import sys
input = sys.stdin.readline
H,W,D = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
Q = int(input())
LR = [tuple(map(int,input().split())) for i in range(Q)]

INF = float('inf')
h = 0--(H*W+1)//D

pos = [[INF]*h for _ in range(D)]
for i,row in enumerate(A):
    for j,a in enumerate(row):
        d,m = divmod(a,D)
        pos[m][d] = (i,j)

dists = [[0] for _ in range(D)]
for i,p in enumerate(pos):
    for p1,p2 in zip(p,p[1:]):
        if p1==INF or p2==INF: continue
        a1,b1 = p1
        a2,b2 = p2
        dist = abs(a1-a2) + abs(b1-b2)
        dists[i].append(dists[i][-1] + dist)

ans = []
for l,r in LR:
    a,i = divmod(l,D)
    b,j = divmod(r,D)
    if i==0:
        a-=1; b-=1
    ans.append(dists[i][b] - dists[i][a])
print(*ans, sep='\n')