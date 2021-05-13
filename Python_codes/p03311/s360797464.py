N=int(input())
A=list(map(int,input().split()))

for i in range(1,N+1):
  A[i-1]-=i

A.sort()
if N%2==1:
  ma=A[N//2]
  print(sum([abs(i-ma) for i in A]))
else:
  ma=[A[N//2]-1,A[N//2]]
  a=[]
  for m in ma:
    a.append(sum([abs(i-m) for i in A]))
  print(min(a))
