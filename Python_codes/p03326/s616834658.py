import itertools

N,M=map(int,input().split())
x=[[0,0,0] for _ in range(N)]

for i in range(N):
    x[i][0],x[i][1],x[i][2]=map(int,input().split())
    
#+++,++-など8パターン
a=[]
for i in itertools.product([1,-1], repeat=3):
    a.append(i)
dp=[[[0]*(M+1) for _ in range(N+1)] for k in range(8)]#i番目まで，j個使うとき,kパターンの合計の最大

def msum(L,xx):
    ans=0
    for i in range(len(xx)):
        ans+=xx[i]*L[i]
    return ans


for k in range(8):
    for i in range(N):
        for j in range(min(M,i+1)):
            if j==i:
                dp[k][i+1][j+1]=dp[k][i][j]+msum(a[k],x[i])
            else:
                dp[k][i+1][j+1]=max(dp[k][i][j+1],dp[k][i][j]+msum(a[k],x[i]))
            
        
ans=0
for k in range(8):
    ans=max(ans,dp[k][-1][-1])
print(ans)


