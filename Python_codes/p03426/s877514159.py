import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W, d = mapint()
As = [list(mapint()) for _ in range(H)]
Q = int(input())

from collections import defaultdict
from itertools import accumulate
from bisect import bisect_left
dic = defaultdict(list)
for h in range(H):
    for w in range(W):
        a = As[h][w]
        dic[a%d].append((a, h, w))

cost_dic = {}
for m in dic.keys():
    dic[m].sort()
    sa, sh, sw = dic[m][0]
    cost_dic[m] = [0]
    for a, h, w in dic[m][1:]:
        cost = abs(h-sh)+abs(w-sw)
        cost_dic[m].append(cost)
        sa, sh, sw = a, h, w
    cost_dic[m] = list(accumulate(cost_dic[m]))

for _ in range(Q):
    l, r = mapint()
    sidx = bisect_left(dic[l%d], (l, 0, 0))
    eidx = bisect_left(dic[l%d], (r, 0, 0))
    print(cost_dic[l%d][eidx]-cost_dic[l%d][sidx])