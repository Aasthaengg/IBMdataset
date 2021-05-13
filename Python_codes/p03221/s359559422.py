n,m=map(int,input().split())
l=[[] for i in range(n)]
for i in range(m):
  p,y=map(int,input().split())
  l[p-1].append((y,i))

ids=["" for i in range(m)]
for i in range(n):
  l[i].sort()
  for j in range(len(l[i])):
    ids[l[i][j][1]]="{:0>6d}".format(i+1)+"{:0>6d}".format(j+1)
print("\n".join(ids))