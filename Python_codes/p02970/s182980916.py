N,D = map(int,input().split())

n = 2*D +1

if N <= n:
  print(1)
else:
  if N % n == 0:
    print(N//n)
  else:
    print(N//n + 1)