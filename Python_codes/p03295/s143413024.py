n,m=map(int,input().split())
ab=[tuple(map(int,input().split())) for _ in range(m)]
ab.sort(key=lambda x: x[1])
ans=0
t=-1
for a,b in ab:
  if a>=t:
    ans+=1
    t=b
print(ans)