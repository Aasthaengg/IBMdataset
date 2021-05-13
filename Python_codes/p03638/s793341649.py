import sys
input = sys.stdin.readline
H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
c = [[0] * W for _ in range(H)]
tour = [[0] * W for _ in range(H)]
s = []
s.append([0, 0])
ss = []
ss.append([0, 0])
tour[0][0] = 1
t = 0
counter = 1
while counter < H * W:
  counter += 1
  p = s.pop()
  n = [-1, -1]
  while not (0 <= n[0] < H and 0 <= n[1] < W and tour[n[0]][n[1]] == 0):
    if t == 0:
      n = [p[0] + 1, p[1]]
    elif t == 1:
      n = [p[0], p[1] + 1]
    elif t == 2:
      n = [p[0] - 1, p[1]]
    else:
      n = [p[0], p[1] - 1]
    if 0 <= n[0] < H and 0 <= n[1] < W and tour[n[0]][n[1]] == 0:
      break
    else:
      t = (t + 1) % 4
  s.append(n)
  tour[n[0]][n[1]] = tour[p[0]][p[1]] + 1
  ss.append(n)
#print(tour, ss, c)
for i in range(N):
  for _ in range(a[i]):
    p = ss.pop()
    #print(p)
    c[p[0]][p[1]] = i + 1
for i in range(H):
  print(*c[i])