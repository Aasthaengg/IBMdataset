n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
b = [int(input()) for _ in range(m)]
for ni in range(n):
    ans = 0
    for mi in range(m):
        ans += A[ni][mi] * b[mi]
    print(ans)