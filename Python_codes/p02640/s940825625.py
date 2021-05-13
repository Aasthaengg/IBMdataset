N, A = list(map(int, input().split()))

flag = False
for i in range(N+1):
  count = i * 2 + (N - i) * 4
  if count == A:
    flag = True

if flag:
  print('Yes')
else:
  print('No')