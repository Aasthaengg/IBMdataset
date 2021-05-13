n = int(input())
A = list(map(int, input().split()))
B = []
for i in range(n):
    B.append(A[i] - i - 1)
B = sorted(B)

b = B[n//2]

total = 0

for i in B:
    total += abs(i - b)
print(total)