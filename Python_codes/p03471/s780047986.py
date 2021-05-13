N,Y = map(int,input().split())

cnt = 0
for i in range(N+1):
  for j in range(N+1-i):
    k=N-i-j
    if 0 <= k and 10000*i+5000*j+1000*k == Y:
      print(i, j, k)
      cnt += 1
      break
  else:
    continue
  break
if cnt == 0:
  print(-1, -1, -1)