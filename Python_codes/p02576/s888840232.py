N, X, T = map(int, input().split())

time = N // X
if(N%X == 0):
  print(time * T)
else:
  print((time+1) * T)