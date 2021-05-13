A,B,M=map(int,input().split())
a=input().split()
A=list(a)
b=input().split()
B=list(b)
ab=int(min(A))+int(min(B))

X=list()
Y=list()
C=list()
for i in range(M):
  x,y,c=map(int,input().split())
  X.append(x)
  Y.append(y)
  C.append(c)
ans=list()
for i in range(M):
  xx=int(X[i])-1
  yy=int(Y[i])-1
  cc=int(C[i])
  num=int(A[xx])+int(B[yy])-cc
  ans.append(num)
Ans=int(min(ans))
print(min(ab,Ans))