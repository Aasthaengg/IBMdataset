n,m=map(int,input().split())
e=[[]for _ in range(n)]
py=[]
for _ in range(m):
  p,y=map(int,input().split())
  py.append((p,y))
  e[p-1].append(y)
for i in range(n):e[i].sort()
xy=lambda x,y:y*1000000+x
d={}
for i in range(n):
  for j in range(len(e[i])):
    d[xy(i+1,e[i][j])]=str(i+1).zfill(6)+str(j+1).zfill(6)
for p,y in py:
  print(d[xy(p,y)])
