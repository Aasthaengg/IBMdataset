"""
制約がヒントっぽいな。
桁DPで解ける

dp[i][j][k] => 2進数表記でa+bの左からi桁目まで見る。i桁目がjになるような場合の数。kは未満フラグ。配るDPで解く。

"""
L = input()
N = len(L)
mod = 10**9 +7
dp = [[[0]*2 for _ in range(2)]for _ in range(N)]
dp[0][1][0] = 2
for i in range(1,N):
    dp[i][1][1] = 2

for i in range(N-1):
    x = int(L[i+1])
    for j in range(2):
        for k in range(2):
            for l in range(2):
                if not k and l > x:
                    continue
                if k or l < x:
                    nxFlag = 1
                else:
                    nxFlag = 0
                if l == 0:
                    dp[i+1][l][nxFlag] += dp[i][j][k]
                else:
                    dp[i+1][l][nxFlag] += dp[i][j][k]*2
                dp[i+1][l][nxFlag]%=mod
ans = (sum(dp[-1][1])+sum(dp[-1][0])+1)%mod
print(ans)