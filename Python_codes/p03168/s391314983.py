N = int(input())
p_f = [0.0]
p_b = [0.0]
for p in list(map(float,input().split())):
    p_f.append(p)
    p_b.append(1.0-p)

#一次軸：コイントスの回数、二次軸：勝ち数、値：発生確率
dp = [[0.0] * (N+1) for i in range(N+1)]
dp[0][0] = 1.0

def cointoss(n_toss):
    global p_majority
    for i in range(n_toss):
        dp[n_toss][i+1] += dp[n_toss-1][i] * p_f[n_toss]
        dp[n_toss][i  ] += dp[n_toss-1][i] * p_b[n_toss]

for i in range(1,N+1):
    cointoss(i)

p_majority = 0.0
n_majority = N // 2 + 1

for i in range(n_majority,N+1):
    p_majority += dp[N][i]

print(p_majority)