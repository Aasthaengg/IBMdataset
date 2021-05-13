import queue
H , W = list(map(int, input().split()))
S = [input() for _ in range(H)]
Sum = 0
for i in range(H):
  for j in range(W):
    Sum += (S[i][j] == '#')
start = [1, 1, 1]
visited = [[0] * W for _ in range(H)]
visited[0][0] = 1
Q = queue.Queue()
Q.put(start)
now = start
while(now[:2] != [H, W] and not Q.empty()):
  now = Q.get()
  for i in range(2):
    for j in range(2):
      h = now[0] + ((-1) ** i + (-1) ** j) // 2
      w = now[1] + ((-1) ** i - (-1) ** j) // 2
      if(1 <= h and h <= H and 1 <= w and w <= W and visited[h - 1][w - 1] == 0 and S[h - 1][w - 1] == '.'):
        visited[h - 1][w - 1] = 1
        Q.put([h, w, now[2] + 1])
if(now[:2] == [H, W]):
  print(H * W - Sum - now[2])
else:
  print(-1)