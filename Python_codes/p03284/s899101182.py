N, K = tuple(int(num) for num in input().split())

if not N % K:
  print(0)
else:
  print(1)