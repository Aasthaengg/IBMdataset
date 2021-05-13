n=int(input())
#a=[0,a1,a2,a3,...,an]
a=[0]
b=[0]
c=[0]
#０日め　0,0,0
#1日目　a1,b1,c1
#2日目　a2=b1+a2 or c1+a2
dp=[[0 for i in range(3)] for j in range(n+1)]
for i in range(n):
    x,y,z=map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(z)
for i in range(1,n+1):
    dp[i][0]=max(dp[i-1][1]+a[i],dp[i-1][2]+a[i])
    dp[i][1]=max(dp[i-1][0]+b[i],dp[i-1][2]+b[i])
    dp[i][2]=max(dp[i-1][0]+c[i],dp[i-1][1]+c[i])
print(max(dp[n]))