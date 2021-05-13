H,W=map(int, input().split())
S=[]
for i in range(H):
    s=list(input())
    S.append(s)

nowblack=False
dp=[[float("INF")]*W for _ in range(H)]
if S[0][0]=="#":
    dp[0][0]=1
else:
    dp[0][0]=0
for h in range(H):
    for w in range(W):
        if 0<=h-1<H:
            if S[h][w]==".":
                dp[h][w]=min(dp[h][w], dp[h-1][w])
            else:
                if S[h-1][w]=="#":
                    dp[h][w]=min(dp[h][w], dp[h-1][w])
                else:
                    dp[h][w]=min(dp[h][w], dp[h-1][w]+1)


        if 0<=w-1<W:
            if S[h][w]==".":
                dp[h][w]=min(dp[h][w], dp[h][w-1])
            else:
                if S[h][w-1]=="#":
                    dp[h][w]=min(dp[h][w], dp[h][w-1])
                else:
                    dp[h][w]=min(dp[h][w], dp[h][w-1]+1)

print(dp[H-1][W-1])
#print(dp)