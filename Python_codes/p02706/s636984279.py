N,M = list(map(int,input().split()))
n = list(map(int,input().split()))
sn =sum(n)
if N-sn <0:
  print(-1)
else:
  print(N-sn)