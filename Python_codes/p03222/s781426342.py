h,w,k=map(int,input().split())
mod=10**9+7
dp=[[0]*w for _ in range(h)]
D=[[0]*w for _ in range(w)]
for i in range(2**(w-1)):
    s='0'+bin(i)[2:].rjust(w-1,'0')+'0'
    if '11' in s:continue
    for i in range(w-1):
        if s[i+1]=='1':
            D[i][i+1]+=1
            D[i+1][i]+=1
    for i in range(w):
        if s[i:i+2]=='00':
            D[i][i]+=1
dp[0]=D[0]
for i in range(1,h):
    for j in range(1,w):
        dp[i][j]+=dp[i-1][j-1]*D[j-1][j]
    for j in range(w-1):
        dp[i][j]+=dp[i-1][j+1]*D[j+1][j]
    for j in range(w):
        dp[i][j]+=dp[i-1][j]*D[j][j]
        dp[i][j]%=mod
print(dp[-1][k-1])