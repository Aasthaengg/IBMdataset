H, W = map(int, input().split())
S = [input() for _ in range(H)]
 
f = False
for h in range(H):
  pre = '.'
  now = S[h][0]
  nxt = S[h][1]
  abv = '.' if h == 0 else S[h-1][0]
  blw = '.' if h == H-1 else S[h+1][0]
  for w in range(W):
    if now == '.':
      f = False
    elif now in [pre, nxt, abv, blw]:
      f = False
    else:
      f = True
    
    pre = now
    now = nxt
    nxt = '.' if w == W-1 else S[h][w+1]
    abv = '.' if h == 0 else S[h-1][w]
    blw = '.' if h == H-1 else S[h+1][w]
    
    if f:
      print('No')
      exit()
print('Yes')