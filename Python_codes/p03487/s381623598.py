n=int(input())
a=list(map(int,input().split()))
d={}

for x in range(n):
  if a[x] not in d:
    d[a[x]]=0
  d[a[x]]+=1
  
ans=0
for y in d:
  if d[y]>y:
    ans+=d[y]-y
  elif d[y]<y:
    ans+=d[y]
    
print(ans)