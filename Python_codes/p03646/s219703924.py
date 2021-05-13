import sys
input = sys.stdin.readline
N = int(input())
if 50 >= N > 1:
  print(N)
  res = [N] * N
  print(*res)
elif N > 50:
  print(50)
  res = [49] * 50
  t = N // 50
  for i in range(50):
    res[i] += t
  u = N % 50
  if u:
    for i in range(u):
      res[i] += 50 - u + 1
    for i in range(u, 50):
      res[i] -= u
  print(*res)
elif N == 0:
  print(2)
  print(1, 1)
elif N == 1:
  print(2)
  print(2, 0)