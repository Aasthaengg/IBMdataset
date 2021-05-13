S=input()
N=len(S)
Z={}

for i in range(N):
    if S[i] in Z:
        Z[S[i]].append(i)
    else:
        Z[S[i]]=[i]
    
M=float("inf")
for z in Z:
    L=[1*(i in Z[z]) for i in range(N)]

    K=0
    while sum(L)!=len(L):
        K+=1
        for i in range(len(L)-1):
            L[i]=max(L[i],L[i+1])
        L=L[:-1]
    
    M=min(M,K)
print(M)