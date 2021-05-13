n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
d=[]
for _ in range(m):
  d+=[list(map(int,input().split()))[::-1]]
d=sorted(d)[::-1]
j=0
ans=0
flag=1
for i in a:
  if flag and d[j][0]>i:
    ans+=d[j][0]
    d[j][1]-=1
    if d[j][1]==0:j+=1
    if j==m:flag=0
  else:ans+=i
print(ans)