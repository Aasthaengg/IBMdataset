from collections import defaultdict as dd
H,W,N=map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(N)]
tpl = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
edge_WtoB = dd(int)
edge_BtoB = dd(int)
node_B = set(ab)
# node_W = set()
res = dd(int)
# 今見てるマスが黒
for a,b in ab:
    for s,t in tpl:
        tgt = (a+s,b+t)
        # 隣接マスも黒
        if tgt in node_B:
            if not (1 < a < H and 1 < b < W):
                continue
            edge_BtoB[(a,b)] += 1
        # 隣接マスは白
        else:
            if not (1 < a + s < H and 1 < b + t < W):
                continue
            edge_WtoB[tgt] += 1
            # node_W.add(tgt)
for val in edge_WtoB.values():
    res[val] += 1
for val in edge_BtoB.values():
    res[val] += 1
zero = (H-2)*(W-2)
for j in range(1,10):
    zero -= res[j]
res[0] = zero
for j in range(10):
    print(res[j])