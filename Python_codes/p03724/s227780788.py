N, M = map(int, input().split())
l = [0] * (N+1)
for i in range(M):
  a, b = map(int, input().split())
  l[a] += 1
  l[b] += 1
  
flag = True
for i in range(N+1):
  if l[i] % 2 == 1:
    flag = False
    break
if flag:
  print('YES')
else:
  print('NO')