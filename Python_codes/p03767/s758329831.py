n = int(input())
A = list(map(int, input().split()))

A = sorted(A)[::-1]
ans = 0

for i in range(1, 2*n, 2):
    ans += A[i]

print(ans)
