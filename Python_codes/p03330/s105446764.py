import collections
INF = 10**10
N,C=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(C)]
c=[list(map(int,input().split())) for _ in range(N)]
lc= [[],[],[]]
for i in range(N):
    for j in range(N):
        lc[(i+j) % 3].append(c[i][j])
clc = [collections.Counter(lc[i]) for i in range(3)]

def iwakan(clist,color):
    global C
    ret = 0
    for i in range(C):
        ret += clist[i+1] * d[i][color]
    return ret

res = INF
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or i == k or j == k:
                continue
            res = min(res,iwakan(clc[0],i)+iwakan(clc[1],j)+iwakan(clc[2],k))

print(res)