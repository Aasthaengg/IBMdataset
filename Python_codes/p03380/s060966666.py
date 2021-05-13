N=int(input())
A=list(map(int,input().split()))
A.sort()

def binary(l,i):
  r=N-1
  while l<=r:
    m=(l+r)//2
    if A[m]==i:
      return A[m]
    elif A[m]>i:
      r=m-1
    else:
      l=m+1
  x=abs(A[m]-i)
  for j in range(max(0,m-2),min(m+3,N-1)):
    if x >= abs(A[j]-i):
      res = A[j]     
      x=abs(A[j]-i)
  return res


print(A[-1],binary(1,A[-1]/2))