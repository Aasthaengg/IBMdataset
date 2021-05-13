N=int(input())
X=list(map(int,input().split()))
Y=sorted(X)

alpha=Y[N//2-1]
beta=Y[N//2]

S=[0]*N
for k in range(N):
    x=X[k]
    if x<=alpha:
        S[k]=beta
    else:
        S[k]=alpha

print("\n".join(map(str,S)))
