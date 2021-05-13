n,k=map(int,input().split())
A=list(map(int,input().split()))
i=l=1
l=0
F=[0]*n
L=[]
while 1:
  i=A[i-1]
  if F[i-1]>0:
    break
  else:
    L.append(i)
    F[i-1]=l
    l+=1
print((L[F[i-1]:])[(k-F[i-1])%(l-F[i-1])-1] if k>F[i-1] else L[k-1])