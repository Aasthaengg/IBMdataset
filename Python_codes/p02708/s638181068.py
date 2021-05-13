N, K = list(map(int,input().split()))
ans = 0
INF = 10 ** 9 + 7
for i in range(K, N + 2):
    mi = i * (i - 1) // 2
    ma = i * (2 * N - i + 1) // 2
    ans += ma - mi + 1
    ans %= INF
print(ans)