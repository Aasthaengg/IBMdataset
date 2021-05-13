N,M=map(int,input().split())

S={}
T=[0]*(N+1)
F=[0]*M
for i in range(M):
    P,Y=map(int,input().split())
    F[i]=(P,Y)
    S[(P,Y)]=i
    T[P]+=1

U=[0]*(N+1)
X=[[0]*T[i] for i in range(N+1)]

for P,Y in F:
    X[P][U[P]]=Y
    U[P]+=1

H=[""]*M

for i in range(N+1):
    X[i].sort()

    for j in range(T[i]):
        g=S[(i,X[i][j])]
        H[g]=str(i).zfill(6)+str(j+1).zfill(6)
        j+=1
print("\n".join(H))