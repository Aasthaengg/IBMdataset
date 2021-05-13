import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

#木なので一度に隣り合うマスを全て塗っても答えは同じ
N = ir()
edges = [[] for _ in range(N+1)] #1-indexed
for _ in range(N-1):
    a, b = lr()
    edges[a].append(b)
    edges[b].append(a)

fen = 0
snu = 0
used = set([1, N])
fen_list = [1]
snu_list = [N]
while fen_list or snu_list:
    f = []
    for x in fen_list:
        for next in edges[x]:
            if next in used:
                continue
            fen += 1
            f.append(next)
            used.add(next)
    fen_list = f
    s = []
    for y in snu_list:
        for next in edges[y]:
            if next in used:
                continue
            snu += 1
            s.append(next)
            used.add(next)
    snu_list = s

print('Fennec' if fen > snu else 'Snuke')
# 46