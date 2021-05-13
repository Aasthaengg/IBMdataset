#d
X,Y,Z,K = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
C.sort(reverse=True)

ab = sorted([aa+bb for aa in A for bb in B ],reverse=True)[:K]
ans = sorted([aabb+cc for aabb in ab for cc in C ],reverse=True)[:K]

for aa in ans:
    print(aa)