D,G=map(int,input().split())
G//=100

P=[0]*(D+1)
C=[0]*(D+1)

for i in range(1,D+1):
    p,c=map(int,input().split())
    P[i]=p
    C[i]=c//100

Min_Solved=float("inf")

for i in range(2**D):
    Rest=G
    Solved=0

    A=[0]*(D+1)

    x=i
    for j in range(1,D+1):
        A[j]=x%2
        if x%2:
            Rest-=j*P[j]+C[j]
            Solved+=P[j]
        x>>=1

    for k in range(D,0,-1):
        if Rest<=0:
            break

        if A[k]==0:
            if k*P[k]<=Rest:
                Rest-=k*P[k]+C[k]
                Solved+=P[k]
            else:
                z=(Rest+(k-1))//k
                Rest-=k*z
                Solved+=z

    Min_Solved=min(Min_Solved,Solved)
    assert 1

print(Min_Solved)