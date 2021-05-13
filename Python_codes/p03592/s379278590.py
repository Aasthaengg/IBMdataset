N, M, K = list(map(int, input().split()))

k = 0
flag = False
for i in range(N+1):
  for j in range(M+1):
    k = (N-i) * j + (M-j) * i
    if k == K:
      flag = True
      break
  if flag:
    break

if flag:
  print('Yes')
else:
  print('No')