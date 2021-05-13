n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(n)]

ans=0
for i in [-1,1]:
  for j in [-1,1]:
    for k in [-1,1]:
      l=[]
      for x,y,z in xyz:
        l.append(i*x+j*y+k*z)
      l.sort(reverse=True)
      ans=max(ans,sum(l[:m]))
print(ans)