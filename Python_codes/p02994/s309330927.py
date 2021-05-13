N,L=map(int,input().split())
A=L
if L<=0 and L-1+N>=0:
  A=0
elif L<=0:
  A=L+N-1
print(N*(N-1)//2+L*N-A)