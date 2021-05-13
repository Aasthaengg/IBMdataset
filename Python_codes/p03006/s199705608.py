import copy

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
ans = 10**10
for i in range(N-1):
  x_begin, y_begin = XY[i]
  for j in range(i+1, N):
    p = XY[j][0]-XY[i][0]
    q = XY[j][1]-XY[i][1]
    c = 0
    for k in range(N-1):
      for l in range(k+1, N):
        dx = XY[k][0]-XY[l][0]
        dy = XY[k][1]-XY[l][1]
        if dx == p and dy == q or dx == -p and dy == -q:
          c += 1
    ans = min(ans, N-c)
print(ans if N > 2 else 1)