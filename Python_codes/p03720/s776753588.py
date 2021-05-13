def pathnumber(N, M) : 
  path = [0] * (N + 1)
  for i in range(M) : 
    x, y = tuple(map(int, input().split()))
    path[x] += 1 
    path[y] += 1
  return path

N, M = tuple(map(int, input().split()))

path = pathnumber(N, M)

for i in range(1, N + 1) : 
  print(path[i])
  
