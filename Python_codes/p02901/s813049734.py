### 提出 #10098255

##頭良すぎて草

##x | y    x と y のビット単位 論理和
##x ^ y    x と y のビット単位 排他的論理和
##x & y    x と y のビット単位 論理積
##x << n   x の n ビット左シフト
##x >> n   x の n ビット右シフト
##~x       x のビット反転

n,m=map(int,input().split())
p=2**n
inf=10**9
dp=[inf]*p
dp[0]=0
for i in range(m):
    a,b=map(int,input().split())
    c=sum([2**(j-1) for j in list(map(int,input().split()))])
    for k in range(p):
        if dp[k|c]>dp[k]+a:
            dp[k|c]=dp[k]+a
print(dp[-1] if dp[-1]!=inf else -1)
