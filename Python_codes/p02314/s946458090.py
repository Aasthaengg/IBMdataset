import math
n, m = map(int,input().split(' '))
d = list(map(int,input().split(' ')))
d.sort()
inf = n

dp = [ [ inf for i in range(m+1)] for j in range(n+1) ]

# dp
for j in range(m+1):
    dp[0][j]=0

for j in range(m-1,-1,-1):
    for i in range(n+1):
        #for k in range(math.floor(i/d[j])+1):
        if math.floor(i/d[j]) >=1:
            k=1
        else:
            k=0
        r = k*d[j]
        #print(i,j,k)
        dp[i][j] = min( dp[i][j], dp[i][j+1], dp[i-r][j]+k ) 
        #print("dp:",i,j,dp[i][j])
print(dp[n][0])

