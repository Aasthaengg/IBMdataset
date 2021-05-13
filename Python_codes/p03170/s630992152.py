from sys import stdin,stdout
n,k=map(int,stdin.readline().split())
a=list(map(int,stdin.readline().split()))
dp=[[-1,-1] for i in range(k+1)]
for i in range(1,k+1):
    for j in a:
        if i>=j:
            if dp[i-j][0]==-1 and dp[i-j][1]==-1:
                dp[i][0]=1
            elif dp[i-j][1]==1:
                dp[i][0]=1
    if dp[i][0]==-1:
        dp[i][1]=1
if dp[k][0]==1:
    print('First')
else:
    print('Second')
# print(dp)