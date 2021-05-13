N=int(input())
C=[int(input()) for _ in range(N)]
C=[0]+[c for i,c in enumerate(C) if i==0 or C[i-1]!=c]
MOD=10**9+7

#dp[i]=インデックスiまででの塗り方の数
dp=[0]*(len(C))
dp[0]=1
import collections
memo=collections.defaultdict(int)
for i in range(1,len(dp)):
    dp[i]=(dp[i-1]+memo[C[i]])%MOD
    memo[C[i]]=(memo[C[i]]+dp[i-1])%MOD

print(dp[len(C)-1])

#print(dp)