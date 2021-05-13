N,X,T = map(int, input().split())
n = N%X
if n == 0:
  print(int(N/X)*T)
else:
  print(int(N/X+1)*T)