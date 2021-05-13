H, W=map(int, input().split())
c=['.'*(W+2)]+['.'+input()+'.' for _ in range(H)]+['.'*(W+2)]
ans=[['0']*(W+2) for _ in range(H+2)]
for h in range(1, H+1):
  for w in range(1, W+1):
    if c[h][w]=='#':
      ans[h][w]='#'
    else:
      x=0
      if c[h-1][w-1]=='#':
        x+=1
      if c[h-1][w]=='#':
        x+=1
      if c[h-1][w+1]=='#':
        x+=1
      if c[h][w-1]=='#':
        x+=1
      if c[h][w+1]=='#':
        x+=1
      if c[h+1][w-1]=='#':
        x+=1
      if c[h+1][w]=='#':
        x+=1
      if c[h+1][w+1]=='#':
        x+=1
      ans[h][w]=str(x)
for i in range(1, H+1):
  print(''.join(ans[i][1:-1]))