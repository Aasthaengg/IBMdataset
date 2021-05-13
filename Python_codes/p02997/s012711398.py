N, K = map(int, input().split())

n = (N-1)*(N-2) // 2 - K

if n < 0:
  print(-1)
else:
  M = N-1 + n
  print(M)
  for i in range(2, N+1):
    print(1, i)
  
  if n > 0:
    count = 0
    for i in range(2, N+1):
      for j in range(i+1, N+1):
        print(i, j)
        count += 1
        if count == n:
          break

      if count == n:
        break