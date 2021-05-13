import sys


fin = sys.stdin.readline
MOD = 10**9 + 7
N = int(fin())
C_list = tuple(int(fin()) for _ in range(N))

dp = [0] * N
dp[0] = 1
past_idx = {C_list[0]: 0}
for i, C in enumerate(C_list[1:], start=1):
    if C in past_idx:
        dp[i] = dp[i - 1] + dp[past_idx[C]] if i - past_idx[C] > 1 else dp[i - 1]

    else:
        dp[i] = dp[i - 1]
    past_idx[C] = i
    dp[i] %= MOD
# print(dp)
print(dp[-1])
