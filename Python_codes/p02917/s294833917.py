N=int(input())
B=list(map(int,input().split()))
A=[-1]*N
x,y=0,0
for a in B:
  y=x+1
  if A[x]==-1:
    A[x]=a
    A[y]=a
  else:
    if A[x]>a:
      A[x]=a
    A[y]=a
  x+=1
print(sum(A))
