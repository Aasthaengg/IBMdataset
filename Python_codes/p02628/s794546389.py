N,K=map(int,input().split())
P=list(input().split())
Ps=[int(s) for s in P]
Ps.sort()
Psx=Ps[:K]


print(sum(Psx))
