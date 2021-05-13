#C
N = int(input())
a = [0] * N
b = [0] * N
c = [0] * N
for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())
dp=[[0 for i in range(3)] for j in range(N+1)]
dp[1][0]=a[0]
dp[1][1]=b[0]
dp[1][2]=c[0]
for i in range(2,N+1):    
    for j in range(3):
        if j==0:
            w=a[i-1]
        elif j==1:
            w=b[i-1]
        else:
            w=c[i-1]
        dp[i][j]=max(dp[i-1][(j+1)%3]+w,dp[i-1][(j+2)%3]+w)
print(max(dp[-1])) 