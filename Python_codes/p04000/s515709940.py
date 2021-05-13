H, W, N = map(int, input().split())
S = {}
for i in range(N):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  for i in range(max(0, a-1), min(H, a+2)):
    for j in range(max(0, b-1), min(W, b+2)):
      if (i, j) not in S: S[(i, j)] = 0
      S[(i, j)] += 1
rs = [0]*10
rs[0] = (H-2)*(W-2)
for (i, j) in S:
  if i > 0 and j > 0 and i < H-1 and j < W-1:
    n = S[(i, j)]
    #print(i, j, n)
    rs[0] -= 1
    rs[n] += 1
for j in range(0, 9+1):
  r = rs[j]
  print(r)
