N, K = map(int, input().split(' '))
count = (N - 1) * (N - 2) // 2
is_connect = [[False for _ in range(N)] for _ in range(N)]
if K > count:
  print(-1)
else:
  for i in range(1, N):
    is_connect[0][i] = True
  i = 2
  j = 1
  for _ in range(count - K):
    is_connect[j][i] = True
    if i == N - 1:
      j += 1
      i = j + 1
    else:
      i += 1
  print(N - 1 + count - K)
  for i in range(N):
    for j in range(N):
      if i != j and is_connect[i][j]:
        print('{0} {1}'.format(i + 1, j + 1))