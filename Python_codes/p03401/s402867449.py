N=int(input())
A=list(map(int,input().split()))+[0]
csum=[abs(A[i]-A[i-1]) for i in range(N+1)]
csum=sum(csum)
cdiff=[abs(A[i+1]-A[i-1])-abs(A[i]-A[i-1])-abs(A[i+1]-A[i]) for i in range(N)]
for _ in cdiff:
  print(csum+_)