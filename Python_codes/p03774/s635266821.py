def f(X,Y):
    return abs(X[0]-Y[0])+abs(X[1]-Y[1])

inf=float("inf")
N,M=map(int,input().split())

P=[]
for _ in range(N):
    a,b=map(int,input().split())
    P.append((a,b))

Q=[("*","*")]
for _ in range(M):
    c,d=map(int,input().split())
    Q.append((c,d))

S=[]
for X in P:
    D=inf
    J=0
    for k in range(1,M+1):
        if D>f(X,Q[k]):
            D=f(X,Q[k])
            J=k

    S.append(J)

print("\n".join(map(str,S)))
