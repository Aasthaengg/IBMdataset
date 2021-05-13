N,M=map(int,input().split())
price_value = []
for _ in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    v = ["0"]*N
    for i in range(N):
        if i+1 in c:
            v[i] = "1"
    v = "".join(v)
    v = int(v, base=2)
    price_value.append((a, v))

INF = float("inf")
dp = [[INF] * (2**N) for _ in range(M+1)]
dp[0][0] = 0
for i in range(1, M+1):
    price, value = price_value[i-1]
    for j in range(2**N):
        dp[i][j | value] = min(
            dp[i][j | value], dp[i-1][j] + price
        )
        dp[i][j] = min(dp[i][j], dp[i-1][j])
ans = dp[-1][-1]
print(ans if ans != INF else -1)