n,m=map(int,input().split())
ab=[list(map(int,input().split()))for _ in range(m)]
ab.sort()
l=-1;r=n
ans=1
for a,b in ab:
  if b<=l or r<=a:
    ans+=1
    l,r=a,b
  l=max(l,a)
  r=min(b,r)
print(ans)