from numpy import *
N = int(input())
A = list(map(int,input().split()))
print(2*N-1)

if abs(max(A))<abs(min(A)):
  x = argmin(A)
  for n in range(N):
    print(x+1,n+1)
  for n in range(N-1):
    print(N-n,N-n-1)
else:
  x = argmax(A)
  for n in range(N):
    print(x+1,n+1)
  for n in range(N-1):
    print(n+1,n+2)