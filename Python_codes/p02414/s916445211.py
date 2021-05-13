n,m,l= map(int,input().split())
b=[]
A=[]
B=[]
for i in range(n):
        A1=list(map(int,input().split()))
        A.append(A1)
for i in range(m):
        B1=list(map(int,input().split()))
        B.append(B1)
C= [[0 for i in range(l)] for j in range(n)]
for i in range(n):
    for j in range(l):
       for k in range(m):
            C[i][j]+=(A[i][k]*B[k][j])
for i in range(n):
    c=map(str,C[i])
    print(" ".join(c))