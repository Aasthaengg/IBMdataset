# 47 A - Biscuits
N,P = map(int,input().split())
A = list(map(int,input().split()))
A = sorted(A,reverse = False)

# dp[i][p] i 番目までの袋を使ったときに余り p になる選び方
dp = [[0]*2 for _ in range(N+1)]

# 初期条件 (何も選ばないとき余りは 0)
dp[0] = [1,0]

for v in range(1,N+1):
    # 偶数の袋 (偶数を足しても足さなくても偶奇は変わらない)
    if A[v-1]%2 == 0:
        dp[v][0] = dp[v-1][0]*2
        dp[v][1] = dp[v-1][1]*2
    # 奇数の袋 (足すと偶奇が反転する)
    else:
        # 奇数の袋を選んだとき + 選ばなかったとき
        dp[v][0] = dp[v-1][1] + dp[v-1][0]
        dp[v][1] = dp[v-1][0] + dp[v-1][1]
print(dp[N][P])