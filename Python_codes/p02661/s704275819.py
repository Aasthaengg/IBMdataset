n = int(input())
A, B = [0] * n, [0] * n
for i in range(n):
    A[i],B[i] = map(int, input().split())

A.sort()
B.sort()
ans = 0
if n % 2 == 1:
    ans = B[n // 2] - A[n // 2] + 1
else:
    large = B[n // 2] + B[n // 2 - 1]
    small = A[n // 2] + A[n // 2 - 1]
    ans = large - small + 1

print(ans)
