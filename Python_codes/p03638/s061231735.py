H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
M = [[0 for i in range(W)] for j in range(H)]
p = [0, 0]
x = 0
for i in range(N):
  for j in range(A[i]):
    M[p[0]][p[1]] = i+1
    x += 1
    if x % W == 0:
      p[0] += 1
    else:
      if (x // W) % 2 == 0:
        p[1] += 1
      else:
        p[1] -= 1
for i in range(H):
  for j in range(W-1):
    print(M[i][j], end = ' ')
  print(M[i][W-1])