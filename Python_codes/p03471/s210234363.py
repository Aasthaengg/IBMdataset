N,Y = map(int,input().split())

for i in range(N+1):
  for s in range(N+1):
    k = N-i-s
    if k>=0 and 1000*i+5000*s+10000*k==Y:
      print(k,s,i)
      exit()

print(-1,-1,-1)