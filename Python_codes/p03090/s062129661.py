N = int(input())
g = [ [1] * N for _ in range(N) ]

if N % 2 == 1:
  for i in range(N//2):
    g[i][N-2-i] = 0
    g[N-2-i][i] = 0
else:
  for i in range(N//2):
    g[i][N-1-i] = 0
    g[N-1-i][i] = 0
    

M = 0
for b in range(N):
  for a in range(b):
    if g[a][b] == 1:
      M += 1
print(M)
for b in range(N):
  for a in range(b):
    if g[a][b] == 1:
      print(a+1, b+1)

