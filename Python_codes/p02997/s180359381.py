N, K = map(int, input().split())
if 2 * K > (N - 1) * (N - 2):
  print(-1)
else:
  M = N - 1
  D = {1: [_ for _ in range(2, N+1)]}
  cnt = ((N - 1) * (N - 2)) // 2
  pnt = 2
  qnt = 3
  while cnt != K:
    cnt -= 1
    if pnt in D:
      D[pnt].append(qnt)
    else:
      D[pnt] = [qnt]
    qnt += 1
    if qnt == N + 1:
      pnt += 1
      qnt = pnt + 1
    M += 1
  print(M)
  for i in D:
    for j in D[i]:
      print(i, j)