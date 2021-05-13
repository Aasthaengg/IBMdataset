n, x=map(int, input().split())
c=list(map(int, input().split()))
c.sort()
ans=0
for i in range(n-1):
  if c[i]<=x:
    x-=c[i]
    ans+=1
  else:
    break
if c[n-1]==x:
  ans+=1

print(ans)