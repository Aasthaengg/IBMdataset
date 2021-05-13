S = input()
MOD = 10**9+7
N = 13
mul = 1

#dp[k] -> 13で割ったあまりがkのパターン数
dp = [0] * N
dp[0] = 1

#後ろから解くアルゴリズム
# 1?2?3 : 0 -> 3 -> ?3 -> 2?3 -> ...
for i in range(len(S)-1, -1, -1):
    #次の状態
    next_dp = [0] * N
    c = S[i]

    if c == "?":
        for k in range(10):
            for j in range(N):
                next_dp[(k * mul + j) % N] += dp[j]
                next_dp[(k * mul + j) % N] %= MOD

    else:
        k = int(S[i])
        for j in range(N):
            next_dp[(k * mul + j) % N] += dp[j]
            next_dp[(k * mul + j) % N] %= MOD

    mul *= 10
    mul %= N
    dp = next_dp

print(dp[5])
