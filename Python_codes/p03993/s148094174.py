n = int(input())
A = list(map(int, input().split()))
A = [a - 1 for a in A]
count = 0
for i, a in enumerate(A):
	if A[a] == i:
		count += 1
print(count//2)