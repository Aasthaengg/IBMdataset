n,m=map(int,input().split())
a=list(map(int,input().split()))
x=[2,5,5,4,5,6,3,7,6]
dp=[0 for i in range(n+1)]
for i in range(1,n+1):
  l=[-99999999]
  for j in range(m):
    if i-x[a[j]-1]>=0:
      l.append(dp[i-x[a[j]-1]]+1)
  dp[i]=max(l)

a.sort()
a.reverse()
ans=[]
y=n
for i in range(dp[n],0,-1):
  for j in range(m):
    if y-x[a[j]-1]>=0:
      if dp[y-x[a[j]-1]]>=i-1:
        ans.append(str(a[j]))
        y-=x[a[j]-1]
        break
print(''.join(ans))