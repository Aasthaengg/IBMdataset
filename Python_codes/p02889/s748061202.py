N, M, L = map(int,input().split())
MAX=99999999999
A=[]
B=[]
C=[]
D=[[MAX for _ in range(N)] for _ in range(N)]
F=[[MAX for _ in range(N)] for _ in range(N)]
s=[]
t=[]
 
for i in range(M):
    l=list(map(int,input().split()))
    A.append(l[0]-1)
    B.append(l[1]-1)
    C.append(l[2])
 
 
 
Q=int(input())
 
for i in range(Q):
    m=list(map(int,input().split()))
    s.append(m[0]-1)
    t.append(m[1]-1)
 
 
for i in range(M):
    if C[i]>L : continue
    D[A[i]][B[i]]=C[i]
    D[B[i]][A[i]]=C[i]
 
for i in range(N):  D[i][i]=0
 
for k in range(N):
    for i in range(N):
        for j in range(N):
            if (D[i][k]+D[k][j])<D[i][j] :
                D[i][j]=D[i][k]+D[k][j]
 
for i in range(N):
    for j in range(N):
        if i==j : continue
        if D[i][j]<=L: F[i][j]=1
 
 
for i in range(N):  F[i][i]=0
 
for k in range(N):
    for i in range(N):
        for j in range(N):
            if (F[i][k]+F[k][j])<F[i][j] :
                F[i][j]=F[i][k]+F[k][j]
 
 
for p in range(Q) :
    if F[s[p]][t[p]] < MAX :
        print(F[s[p]][t[p]]-1)
    else :
        print(-1)