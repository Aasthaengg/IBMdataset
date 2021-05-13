# coding: utf-8
# Your code here!
H,W=map(int,input().split())

meizu=[]
for _ in range(H):
    meizu.append(list(input()))

dp=[[10**9 for w in range(W)] for h in range(H)]
dp[0][0]=1 if meizu[0][0]=="#" else 0

for h in range(H):
    for w in range(W):
        if h!=H-1:
            dp[h+1][w]=min(dp[h+1][w],dp[h][w]+1 if meizu[h+1][w]=="#" and meizu[h][w]=="." else dp[h][w])
        if w!=W-1:
            dp[h][w+1]=min(dp[h][w+1],dp[h][w]+1 if meizu[h][w+1]=="#" and meizu[h][w]=="." else dp[h][w])
    
print(dp[-1][-1])
