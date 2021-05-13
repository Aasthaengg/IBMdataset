import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W, D = mapint()
As = [list(mapint()) for _ in range(H)]

points = [0]*(H*W)
for i in range(H):
    for j in range(W):
        points[As[i][j]-1] = (i, j)
from collections import defaultdict
from itertools import accumulate
dic = defaultdict(list)

for i in range(1, D+1):
    h, w = points[i-1]
    cnt = 0
    while i+cnt*D<=H*W:
        h2, w2 = points[i+cnt*D-1]
        dic[i].append(abs(h2-h)+abs(w2-w))
        h, w = h2, w2
        cnt += 1
    dic[i] = list(accumulate(dic[i]))

Q = int(input())
for _ in range(Q):
    L, R = mapint()
    base = L%D
    if base==0:
        base = D
    l = (L-base)//D
    r = (R-base)//D
    print(dic[base][r]-dic[base][l])