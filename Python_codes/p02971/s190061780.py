N = int(input())
A= [int(input()) for i in range(N)]

B=sorted(A,reverse=True)
A1=B[0]
A2=B[1]

for i in range(N):
  if A[i]==A1:
    print(A2)
  else:
    print(A1)

