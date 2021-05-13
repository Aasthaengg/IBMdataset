N, M = map(int, input().split())
A=[]
B=[]
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C=[0]*(N+1)

for i in range(M):
    C[A[i]]+=1
    C[B[i]]+=1

for i in range(1,N+1):
    print(C[i])