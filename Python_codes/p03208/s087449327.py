n,k=map(int,input().split())
a=[]
for x in range(n):
  a.append(int(input()))
ans=1000000009
a=sorted(a)
for y in range(n-k+1):
  ans=min(a[y+k-1]-a[y],ans)
  
print(ans)

