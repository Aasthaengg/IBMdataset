H,W,K=map(int,input().split())
if W==1:
    print(1)
    exit()
dp=[[0]*W for _ in range(H+1)]

dp[0][0]=1
import itertools
A=list(itertools.product([1,0],repeat=W-1))
#print(A)
B=[]

for a in A:
    flg=True
    for i in range(len(a)-1):
        if a[i+1]==1 and a[i]==1:
            flg=False
    if flg:
        B.append(a)
#print(B)
for h in range(1,H+1):
    for b in B:
        for w in range(W):
            if w==0:
                dp[h][w]+=dp[h-1][w]*(1-b[w])+dp[h-1][w+1]*b[w]
            elif w==W-1:
                dp[h][w]+=dp[h-1][w]*(1-b[w-1])+dp[h-1][w-1]*b[w-1]
            else:
                dp[h][w]+=dp[h-1][w]*(1-b[w-1])*(1-b[w])+dp[h-1][w-1]*b[w-1]+dp[h-1][w+1]*b[w]
#print(dp)
#print(dp[H-1][K-1])
print(dp[H][K-1]%1000000007)
