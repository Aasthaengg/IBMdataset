#ABC129-E Sum Equals Xor
"""
a+b = a^b
となる場合は、全2進数桁iに対して、
a[i] nand b[i] &1 を満たす場合になる
これは各桁に対してa[i]==b[i]==1を除く2**2-1の3通りが存在するので、
多分桁dpで制約あり/なしを求めてけば求まる
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
mod = 10**9+7
s = readline().rstrip().decode('utf-8')

################################
###########桁DP#################
################################

dp = [[0]*2 for i in range(len(s)+2)]
dp[0][0] = 1 #初期化



for i in range(len(s)):
    for j in range(2): #制約有り、なし
        nd = int(s[i])
        for d in range(3): #00,01,10 (11は条件を満たさない)
            ni = i+1
            nj = j
            if j == 0:
                if nd==0 and d > 0:continue #条件を満たさない
                elif nd == 1 and d==0:nj=1 #条件が必要なくなる遷移

            dp[ni][nj] += dp[i][j]
            dp[ni][nj]%=mod



ans = (dp[ni][0] + dp[ni][1])%mod
print(ans)