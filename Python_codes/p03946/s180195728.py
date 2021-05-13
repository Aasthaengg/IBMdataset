n,t=map(int,input().split())
a=list(map(int,input().split()))
m=10**18
d={}
for i in a:
  if i<m:m=i
  if d.get(i-m):d[i-m]+=1
  else:d[i-m]=1
print(d[max(d)])