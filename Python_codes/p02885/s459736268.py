N = list(map(int,input().split(" ")))

if N[1]*2 >= N[0]:
  print(0)
else:
  print(N[0]-N[1]*2)