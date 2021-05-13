N = int(input())
hn = [int(i) for i in input().split()]



hi_2 = hn[0]
hi_1 = hn[1]
hi = -1

dp = [-1 for _ in range(N)]
dp_2 = dp[0] = 0
dp_1 = dp[1] = abs(hi_2 - hi_1)

for i in range(2, N):
    hi = hn[i]
    dp_i = dp[i] = min(abs(hi - hi_2) + dp_2, abs(hi - hi_1) + dp_1)

    hi_2 = hi_1
    hi_1 = hi
    dp_2 = dp_1
    dp_1 = dp_i

print(dp[N - 1])
