N, K = map(int, input().split())
temp = -1
if N % 2 != 0:
  temp = (N+1)//2
else:
  temp = N // 2
if K > temp:
  print('NO')
else:
  print('YES')