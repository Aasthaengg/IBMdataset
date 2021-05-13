n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(n)]

ans=0
for i in [-1,1]:
  for j in [-1,1]:
    for k in [-1,1]:
      l=[i*xyz[z][0]+j*xyz[z][1]+k*xyz[z][2] for z in range(n)]
      l.sort(reverse=True)
      ans=max(ans,sum(l[:m]))
print(ans)