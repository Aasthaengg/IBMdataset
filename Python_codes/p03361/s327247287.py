H,W = map(int,input().split())
figure = [input() for _ in range(H)]
D = [(1,0), (-1, 0), (0,1), (0,-1)]

for h in range(H):
  for w in range(W):
    if figure[h][w] == '#':
      for dh,dw in D:
        nh, nw = h+dh, w+dw
        if not (0 <= nh <H and 0 <= nw < W):
          continue
        if figure[nh][nw] == '#':
          break
      else:
        print('No')
        exit()
print('Yes')

