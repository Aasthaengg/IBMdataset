N=int(input())
A=[0]+[int(x) for x in input().split()]+[0]

t=sum(abs(A[i]-A[i-1]) for i in range(1,N+2))
for i in range(1,N+1):
  print(t-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))
