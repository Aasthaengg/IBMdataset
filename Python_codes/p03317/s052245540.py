N,K=map(int,input().split())
A=list(map(int,input().split()))
if N<=K:
  print(1)
else:
  i=K
  a=1
  while i<N:
    i+=(K-1)
    a+=1
  print(a)