N,M=map(int,input().split())
ans=0
if(N>=M//2):
  print(M//2)
else:
  print(N+(M-N*2)//4)