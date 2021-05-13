from sys import stdin,stdout
INT_MAX= 10**18
n,k=map(int,stdin.readline().split())
dp  = [INT_MAX]*(n)
h=[int(X) for X in stdin.readline().split()]
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(2,n):
    p=1
    while(p<k+1 and (i-p)>=0):
        dp[i]= min(dp[i-p]+abs(h[i-p]-h[i]),dp[i])
        p+=1
stdout.write(str(dp[n-1])+"\n")
