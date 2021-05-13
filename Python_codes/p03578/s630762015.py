N=int(input())
D=list(map(int, input().split()))
M=int(input())
T=list(map(int, input().split()))
if N<M:
  print('NO')
  exit()
  
A={}
B={}
for i in D:
  if i not in A:
    A[i]=0
  A[i]+=1
  
for i in T:
  if i not in B:
    B[i]=0
  B[i]+=1
  
for i in B.keys():
  if not i in A:
    print('NO')
    exit()
  if A[i]<B[i]:
    print('NO')
    exit()
print('YES')
