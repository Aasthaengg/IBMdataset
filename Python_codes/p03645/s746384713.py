n,m=map(int,input().split())
li=[[] for _ in range(n)]
for i in range(m):
  x,y=map(int,input().split())
  li[x-1].append(y-1)
  li[y-1].append(x-1)
an=[]
for i in li[0]:
  an+=li[i]
if n-1 in an:
  print('POSSIBLE')
else:print('IMPOSSIBLE')