N=int(input())
A=[int(input()) for i in range(N)]
B=[]
while len(A)!=0:
  if A[0] not in B:
    B.append(A[0])
  A.pop(0)
print(len(B))