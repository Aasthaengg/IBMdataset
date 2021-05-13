g=[[*map(int,input().split())]for _ in range(3)]
for h in [0,1]:
  for w in [0,1]: 
    if g[h][w]+g[h+1][w+1]!=g[h+1][w]+g[h][w+1]:
      exit(print('No'))
print('Yes')