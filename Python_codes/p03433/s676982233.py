N, A = [int(input()) for _ in range(2)]
if A < N % 500:
  print('No')
else:
  print('Yes')