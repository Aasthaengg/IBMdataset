N = list(map(int,input().split(" ")))

if N[0] > N[1]:
  if N[0] > 9:
    print(-1)
  else:
    print(N[0]*N[1])
else:
  if N[1] > 9:
    print(-1)
  else:
    print(N[0]*N[1])
