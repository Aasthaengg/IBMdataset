W, H, N = map(int, input().split())
m = [[0] * W for _ in range(H)]
for _ in range(N):
  x, y, a = map(int, input().split())
  if a == 1: 
    for w in range(x):
      for h in range(H):
        m[h][w] = 1
  elif a == 2:
    for w in range(x , W):
      for h in range(H):
        m[h][w] = 1
  elif a == 3:
    for w in range(W):
      for h in range(y):
        m[h][w] = 1
  else:
    for w in range(W):
      for h in range(y, H):
        m[h][w] = 1
print(sum(m, []).count(0))