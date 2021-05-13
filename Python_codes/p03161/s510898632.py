n, k = map(int,input().split())

pedras = list(map(int,input().split()))

INF = 1e12

dp = [INF] * n

dp[0] = 0
dp[1] = abs(pedras[1] - pedras[0])

for i in range(2,n):
    pulo = 0
    for j in range(i-1,-1,-1):
        pulo += 1
        if pulo > k:
            break
        else:
            dp[i] = min(dp[i], dp[j] + abs(pedras[i] - pedras[j]))


print(dp[n-1])
