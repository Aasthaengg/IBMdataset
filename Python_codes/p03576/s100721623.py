import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,K = list(map(int, input().split()))
xy = [tuple(map(int, input().split())) for _ in range(n)]
xs = list(set([item[0] for item in xy]))
ys = list(set([item[1] for item in xy]))
xs.sort()
ys.sort()
dx = {x:i for i,x in enumerate(xs)}
dy = {y:i for i,y in enumerate(ys)}
lx = len(xs)
ly = len(ys)
c = [[0]*ly for _ in range(lx)]
for x,y in xy:
    c[dx[x]][dy[y]] += 1
from itertools import combinations, combinations_with_replacement
def cumsum2(v):
    # v: h*wの2次元リスト
    h,w = len(v), len(v[0])
    v.insert(0, [0]*w)
    for l in v:
        l.insert(0, 0)
    for i in range(1,h+1):
        for j in range(1,w+1):
            v[i][j] = v[i-1][j] + v[i][j-1] - v[i-1][j-1] + v[i][j]
    return v
cumsum2(c)
ans = float("inf")
for i,j,k,l in combinations_with_replacement(range(n),4):
#     for k,l in combinations(range(n),2):
    mx = min(xy[i][0], xy[j][0], xy[k][0], xy[l][0])
    my = min(xy[i][1], xy[j][1], xy[k][1], xy[l][1])
    Mx = max(xy[i][0], xy[j][0], xy[k][0], xy[l][0])
    My = max(xy[i][1], xy[j][1], xy[k][1], xy[l][1])
    ix,iy = dx[mx], dy[my]
    Ix,Iy = dx[Mx], dy[My]
    count = c[Ix+1][Iy+1] - c[Ix+1][iy] - c[ix][Iy+1] + c[ix][iy]
    if count>=K:
        ans = min(ans, (Mx-mx)*(My-my))
#         print(count, i,j,k,l, (Mx-mx)*(My-my))
print(ans)