#Match Matching
n,m=map(int,input().split())
a=list(map(int,input().split()))
lst=[0,2,5,5,4,5,6,3,7,6]
a.sort()
dp=[[0]*(n+1) for i in range(m)]
dq=[[""]*(n+1) for j in range(m)]
x=lst[a[0]]
for i in range(1,n+1):
    if i%x==0:
        dp[0][i]=dp[0][i-x]+1
        dq[0][i]=dq[0][i-x]+str(a[0])
for i in range(1,m):
    x=lst[a[i]]
    for j in range(1,n+1):
        if j<x:
            dp[i][j]=dp[i-1][j]
            dq[i][j]=dq[i-1][j]
        elif j==x:
            if dp[i-1][j]>1:
                dp[i][j]=dp[i-1][j]
                dq[i][j]=dq[i-1][j]
            else:
                dp[i][j]=1
                dq[i][j]=str(a[i])
        else:
            if dp[i][j-x]==0:
                dp[i][j]=dp[i-1][j]
                dq[i][j]=dq[i-1][j]
            else:
                if dp[i-1][j]>dp[i][j-x]+1:
                    dp[i][j]=dp[i-1][j]
                    dq[i][j]=dq[i-1][j]
                elif dp[i][j-x]!=0:
                    dp[i][j]=dp[i][j-x]+1
                    dq[i][j]=dq[i][j-x]+str(a[i])
h=list(map(int,list(dq[m-1][n])))
h.sort(reverse=True)
h=list(map(str,h))
print("".join(h))