N = list(map(int,input().split()))
if N[0]*N[1] >= N[2]*N[3]:
  print(N[0]*N[1])
else:
  print(N[2]*N[3])