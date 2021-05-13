N, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    L = A[i]
    R = A[i + 1]
    eat = max(0, L + R - x)
    ans += eat
    A[i + 1] = max(0, R - eat)

print(ans)