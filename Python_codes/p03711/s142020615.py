a,b = map(int,input().split())

g = [0,2,0,1,0,1,0,0,1,0,1,0]
if g[a-1] == g[b-1]:
  print('Yes')
else:
  print('No')