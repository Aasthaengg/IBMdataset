N, K = map(int, input().split())

rest = N - K
if rest <= 0 or K == 1:
  print(0)
else:
  print(rest)