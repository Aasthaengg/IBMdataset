N=int(input())

A=list(map(int,input().split()))

s=1000//A[0]
m=1000-s*A[0]
am=1000
for i in range(N-1):
  if A[i]<A[i+1]:
    am=m+A[i+1]*s
  else:
    s=am//A[i+1]
    m=am-A[i+1]*s
M=max([s*A[N-1]+m,am])
print(M)