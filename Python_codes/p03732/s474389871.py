n,w=map(int,input().split())
wv=[]
v=[]
for i in range(n):
    a,b=map(int,input().split())
    wv.append([a,b])
    v.append(b)
v.sort(reverse=True)
ans=0
w0=wv[0][0]
wp=3*n+1
dp=[[-1 for jjj in range(n+1)] for iii in range(3*n+1)]
dp[0][0]=0
for i in range(n):
    for jj in range(n-1,-1,-1):
        for k in range(wp-1,-1,-1):
            if dp[k][jj]>=0 and k+wv[i][0]-w0<=wp-1:
                dp[k+wv[i][0]-w0][jj+1]=max(dp[k][jj]+wv[i][1],dp[k+wv[i][0]-w0][jj+1])
for i in range(1,n+1):
    wp=w-w0*i
    if wp<0:
        continue
    elif wp>=3*i:
        ans=max(ans,sum(v[:i]))
    else:
        for j in range(i+1):
            for k in range(wp+1):
                ans=max(dp[k][j],ans)
print(ans)