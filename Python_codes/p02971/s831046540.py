N=int(input())
A=[]
for i in range(N):A.append(int(input()))
B=sorted(A,reverse=True)
b1,b2=B[0],B[1]
for i in range(N):
  if A[i]==b1:print(b2)
  else:print(b1)