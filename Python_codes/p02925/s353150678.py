
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
N = int(input())
A = [[] for _ in range(N)]
for i in range(N):
    A[i] = [i-1 for i in map(int, input().split())]


def pair(x,y):
    if x<y:
        return (x,y)
    else:
        return (y,x)

to_index = dict()
to_pair = dict()
idx = 0
for i in range(N):
    for j in range(i+1,N):
        to_index[(i,j)] = idx
        to_pair[idx] = (i,j)
        idx += 1
    
MAX_N = idx
# DAG TopoSort
in_count = [0]*MAX_N
edge = [[] for _ in range(MAX_N)]

for i in range(N):
    for j in range(N-2):
        vnum = to_index[pair(i,A[i][j+1])]
        pvnum = to_index[pair(i, A[i][j])]
        edge[pvnum].append(vnum)

for i in range(MAX_N):
    for v in edge[i]:
        in_count[v] += 1

S = []
L = [] #Sort結果
index = [0]*MAX_N # 頂点vのLにおけるインデックスindex[v]
ans = 0

for i in range(MAX_N):
    if in_count[i]==0: S.append(i)

while S:
    ans += 1
    new = []
    for _ in range(len(S)):
        v = S.pop()
        index[v] = len(L)
        L.append(v)
        for nv in edge[v]:
            in_count[nv] -= 1
            if in_count[nv]==0:
                new.append(nv)
    S = []
    for n in new:
        S.append(n)


if len(L) != MAX_N:
    print(-1)
    exit()
print(ans)