h,w=map(int,input().split())
s=[list(input()) for i in range(h)]

for y in range(h):
  for x in range(w):
    if s[y][x]=='.':
      cnt=0
      for dy,dx in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]:
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and s[ny][nx]=='#':
          cnt+=1
      s[y][x]=str(cnt)

for i in s:
  print(''.join(i))
