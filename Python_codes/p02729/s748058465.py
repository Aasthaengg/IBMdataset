N, M = map(int, input().split())

if N == 1 and M == 1:
  print(0)
elif N == 0 and M == 1:
  print(0)
elif N == 1 and M == 0:
  print(0)
elif N == 0 and M == 0:
  print(0)
  
else:
  c = N*(N-1) / 2
  d = M*(M-1) / 2
  print(int(c+d))