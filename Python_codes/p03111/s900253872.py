# coding: utf-8
import sys
import itertools

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# N本の竹それぞれA, B, C, 使わないか
N, A, B, C = lr()
bamboo = [ir() for _ in range(N)]
answer = 10 **  5
for pattern in itertools.product(range(4), repeat=N):
    mp = 0
    Alist = []; Blist = []; Clist = []
    for i, p in enumerate(pattern):
        if p == 0:
            Alist.append(bamboo[i])
        elif p == 1:
            Blist.append(bamboo[i])
        elif p == 2:
            Clist.append(bamboo[i])
    if len(Alist) == 0 or len(Blist) == 0 or len(Clist) == 0:
        continue
    mp += 10 * (len(Alist) + len(Blist) + len(Clist) - 3)
    mp += abs(A - sum(Alist)) + abs(B - sum(Blist)) + abs(C - sum(Clist))
    if mp < answer:
        answer = mp

print(answer)
# 04