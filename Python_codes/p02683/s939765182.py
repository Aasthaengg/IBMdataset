from collections import deque
N,M,X=map(int,input().split())
A=[0]*N;cost=0;C=[0]*N;bit=0;v=[0]*M;f=0;minimum=100000*12+1;e=0
for i in range(N):
  a = deque(list(map(int, input().split())))
  C[i]=a[0]
  a.popleft()
  A[i]=a

#print(A[2][2])
#print(C)

for i in range(2**N):
  for j in range(N):
    bit=(1<<j)
    if (i & bit)>0:
      cost+=C[N-1-j]
      for k in range(M):
        v[k]=v[k]+A[N-1-j][k]
  for l in range(M):
    if v[l]<X:
      f=1
     
  if f!=1 and cost<minimum:
    minimum=cost
    e=i
  cost=0;v=[0]*M;f=0
            
print(minimum if minimum!=100000*12+1 else "-1")