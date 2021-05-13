N, K = map(int, input().split())
ans = N

N = N % K
n = abs(N - K)
ans = min(ans, N)
ans = min(ans, n)

print(ans)