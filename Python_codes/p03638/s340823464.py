H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
color = [[0] * W for _ in range(H)]
nowx = 0
nowy = 0
for i in range(N):
  for j in range(a[i]):
    color[nowx][nowy] = i+1
    if(nowx % 2 == 0 and nowy < W-1):
      nowy += 1
    elif(nowx % 2 == 1 and nowy > 0):
      nowy -= 1
    else:
      nowx += 1
      
for h in range(H):
  print(*color[h])