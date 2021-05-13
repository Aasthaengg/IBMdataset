N,R = map(int,input().split())

if(N <= 9):
  print(str(R + 100 * (10 - N)))
else:
  print(str(R))