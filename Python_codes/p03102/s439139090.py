N,M,C=map(int,input().split())
B=list(map(int,input().split()))
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
D=[]
for i in range(N):
    D.append(0)
for i in range(N):
    for j in range(M):
        D[i]+=A[i][j]*B[j]
    D[i]+=C
e=0
for i in range(len(D)):
    if D[i]>0:
        e+=1
print(e)