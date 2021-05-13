N,M=map(int,input().split())

if N>=M//2:
  print(M//2)
else:
  answer=N
  M-=2*N
  N=0
  print(answer+M//4)