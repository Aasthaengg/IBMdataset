N, M, K = map(int, input().split())

flag = False
for i in range(M+1):
  for j in range(N+1):
    tmp = N*i + M*j - 2*i*j
    if tmp == K:
      flag = True
      break
      
if flag:
  print('Yes')
else:
  print('No')