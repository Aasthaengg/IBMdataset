n,p=map(int,input().split())
a=list(map(int,input().split()))
d={0:0,1:0}
for i in range(n):
  d[a[i]%2]+=1
q=2**d[0]
ans=0
m=d[1]
f=[1]
for i in range(1,m+1):
  f+=[f[-1]*i]
for i in range(m+1):
  if i%2!=p:continue
  ans+=q*f[m]//f[i]//f[m-i]
print(ans)