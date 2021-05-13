n = int(input())
A = list(map(int, input().split()))

csum = [0] * n
csum[0] = A[0] 
for i in range(1, n):
	csum [i] = csum[i - 1] + A[i]

mind = 1 << 40
sumA = csum[-1]
for i in range(n):
	diff = abs(sumA - 2 * csum[i])
	mind = min(mind, diff)

print(mind)