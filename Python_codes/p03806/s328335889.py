from fractions import gcd

N,ma,mb=map(int,input().split())
med=[]
for i in range(0,N):
    a,b,c=map(int,input().split())
    med.append((a,b,c))

dp=[[[float("inf") for i in range(0,401)] for j in range(0,401)] for k in range(0,N)]

for i in range(0,401):
    for j in range(0,401):
        if not (i==0 and j==0):
            g=gcd(i,j)
            I=i//g
            J=j//g
            if I==ma and J==mb:
                dp[0][i][j]=0
            else:
                g=gcd(i+med[0][0],j+med[0][1])
                I=(i+med[0][0])//g
                J=(j+med[0][1])//g
                if I==ma and J==mb:
                    dp[0][i][j]=med[0][2]

for i in range(1,N):
    a,b,c=med[i]
    for j in range(0,401-a):
        for k in range(0,401-b):
            dp[i][j][k]=min(dp[i-1][j][k],c+dp[i-1][j+a][k+b])

if dp[N-1][0][0]==float("inf"):
    print(-1)
else:
    print(dp[N-1][0][0])
