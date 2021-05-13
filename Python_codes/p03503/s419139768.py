N=int(input())
J=10

F=[set() for _ in range(N)]
for i in range(N):
    G=list(map(int,input().split()))
    for j in range(J):
        if G[j]:
            F[i].add(j)

P=[[] for _ in range(N)]
for i in range(N):
    P[i]=list(map(int,input().split()))

Ans=-float("inf")
for x in range(1,2**J):
    S=set()
    for t in range(J):
        if x%2:
            S.add(t)
        x>>=1

    Score=0
    for i in range(N):
        Score+=P[i][len(F[i]&S)]
    Ans=max(Ans,Score)
    assert 1

print(Ans)