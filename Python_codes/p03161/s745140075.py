N, K = map(int, input().split())
h = list(map(int, input().split()))

inf = 10000000000

dp = [inf] * N
dp[0] = 0

for i in range(1, N):
    #mindp_i = inf

    for jump in range(1, K + 1):
        if i - jump >= 0:
            dp[i] = min(dp[i], dp[i - jump] + abs(h[i] - h[i - jump]))

            #dpcand = dp[i - jump] + abs(h[i] - h[i - jump])
            #print(dpcand)
            #if dpcand < mindp_i:
            #    mindp_i = dpcand

    #dp[i] = mindp_i

print(dp[N-1])