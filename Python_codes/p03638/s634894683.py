def printans(x):
  for h in range(1, H+1):
    for w in range(1, W+1):
      if w > 1:
        print(' ', end='')
      print(x[h][w], end='')
    print()
		
H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
a.insert(0, -1)

g = [[-1] * (W+2) for x in range(H+2)]
v = 1
for h in range(1, H+1):
  if h%2 != 0:
    for w in range(1, W+1):
      g[h][w] = v
      a[v] -= 1
      if a[v] == 0:
        v += 1
  else:
    for w in range(W, 0, -1):
      g[h][w] = v
      a[v] -= 1
      if a[v] == 0:
        v += 1

printans(g)