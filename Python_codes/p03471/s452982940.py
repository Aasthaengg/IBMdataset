N,Y=map(int,input().split())
for i in range(N+1):
  if 10000*i>Y:
    break
  for j in range(N+1-i):
    k=N-i-j
    S = 10000*i + 5000*j + 1000*k
    if k<0 or S>Y:
      continue
    elif S == Y:
      print(i,j,k)
      exit()
print(-1,-1,-1)
