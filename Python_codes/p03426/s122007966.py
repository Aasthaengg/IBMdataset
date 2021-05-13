import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H, W, d = mapint()
As = [list(mapint()) for _ in range(H)]
Q = int(input())

from collections import defaultdict
dic = {}
for h in range(H):
    for w in range(W):
        a = As[h][w]
        dic[a] = (h, w)

cost_dic = defaultdict(int)
for i in range(d+1, H*W+1):
    oh, ow = dic[i-d]
    h, w = dic[i]
    cost_dic[i] = cost_dic[i-d]+abs(h-oh)+abs(w-ow)

for _ in range(Q):
    l, r = mapint()
    print(cost_dic[r]-cost_dic[l])