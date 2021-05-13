from collections import deque
H, W = map(int, input().split())
R = [[0 for j in range(W)] for i in range(H)]
ans = 0
dx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(H):
  inp = input()
  for j in range(W):
  	if inp[j] == "#":
  	  R[i][j] = 1
for s in range(H * W):
  sh = s // W
  sw = s % W
  if R[sh][sw] == 1:
    continue
  D = [[-1 for j in range(W)] for i in range(H)]
  D[sh][sw] = 0
  d = deque([(sh, sw)])
  while len(d):
    a = d.pop()
    for k in range(4):
      hn = a[0] + dx[k][0]
      wn = a[1] + dx[k][1]
      if 0 <= hn < H and 0 <= wn < W and R[hn][wn] == 0 and D[hn][wn] == -1:
        D[hn][wn] = D[a[0]][a[1]] + 1
        ans = max(ans, D[hn][wn])
        d.appendleft((hn, wn))
print(ans)