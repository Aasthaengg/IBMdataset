H,W,D = map(int,input().split())
A = [tuple(map(int,input().split())) for i in range(H)]
Q = int(input())
LR = [tuple(map(int,input().split())) for i in range(Q)]

pos = [None] * (H*W)
for i,row in enumerate(A):
    for j,a in enumerate(row):
        pos[a-1] = (i,j)

cums = [0]*D
for (x1,y1),(x2,y2) in zip(pos, pos[D:]):
    d = abs(x1-x2) + abs(y1-y2)
    cums.append(cums[-D] + d)

ans = []
for l,r in LR:
    ans.append(cums[r-1] - cums[l-1])
print(*ans,sep='\n')