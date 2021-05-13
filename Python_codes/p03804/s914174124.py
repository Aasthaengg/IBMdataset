N, M = map(int, input().split())
mp1 = [input() for _ in range(N)]
mp2 = [input() for _ in range(M)]

for i in range(N-M+1):
  for j in range(N-M+1):
    f = 1
    for k in range(M):
      for l in range(M):
        if mp2[k][l] != mp1[i+k][j+l]:
          f = 0
          break
      if f == 0:
        break
    if f == 1:
      print('Yes')
      exit()
      
print('No')