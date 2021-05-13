x,y = map(int,input().split())
A=list(map(int,input().split()))
T=sum(A)
a=0
for i in range(x):
  if A[i]>=T/(4*y):
    a+=1
if a>=y:
    print('Yes')
else:
    print('No')
