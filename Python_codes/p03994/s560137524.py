G={chr(a+ord("a")):a for a in range(26)}
H={G[b]:b for b in G}

T=input()
S=[]
for s in T:
    S.append(G[s])
K=int(input())

I=0
N=len(S)
for i in range(N):
    if (i<N-1) and (26-S[i]<=K) and S[i]!=0:
        K-=26-S[i]
        S[i]=0
    elif i==N-1:
        S[i]=(S[i]+(K%26))%26

U=""
for s in S:
    U+=H[s]

print(U)
