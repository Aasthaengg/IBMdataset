N,L = map(int,input().split())
A = []

for n in range(1,N+1):
  A.append(L+n-1)
  
print(sum(A)-min(A,key=abs))