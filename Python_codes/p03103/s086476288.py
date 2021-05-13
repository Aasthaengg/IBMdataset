N,M=map(int,input().split())

D={}
for _ in range(N):
    A,B=map(int,input().split())

    if A in D:
        D[A]+=B
    else:
        D[A]=B

L=[]
for m in D:
    L.append((m,D[m]))

L.sort(key=lambda x:x[0])

S=0
I=0
while M>0:
    (A,B)=L[I]
    B=min(B,M)
    S+=A*B
    M-=B
    I+=1
print(S)
