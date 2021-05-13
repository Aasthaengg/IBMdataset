A,B,N=map(int,input().split())
x=0
if B>N:
  x=N
else:
  x=B-1
  
print(A*x//B)