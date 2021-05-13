#113_D
H,W,K=map(int,input().split())
K-=1
Mod=10**9+7

#row全探索
Row=[]
for i in range(2**(W-1)):
    row=[]
    flg=True
    for j in range(W-1):
        if j>0:
            if (i>>j)&1 and (i>>(j-1))&1:
                flg=False
        row.append((i>>j)&1)
    if flg:
        Row.append(row)
        
Count=[0 for _ in range(W-1)]
for row in Row:
    for i in range(W-1):
        Count[i]+=row[i]

dp=[[0 for _ in range(W)] for _ in range(H+1)]
dp[0][K]=1
if W==1:
    print(1)
    
else:
    for h in range(1,H+1):
        for x in range(W):
            if x==0:
                dp[h][x]=dp[h-1][x]*(len(Row)-Count[x])+dp[h-1][x+1]*Count[x]
            elif x==W-1:
                dp[h][x]=dp[h-1][x]*(len(Row)-Count[x-1])+dp[h-1][x-1]*Count[x-1]
            else:
                dp[h][x]=dp[h-1][x]*(len(Row)-Count[x]-Count[x-1])+dp[h-1][x+1]*Count[x]+dp[h-1][x-1]*Count[x-1]

    print(dp[H][0]%Mod)