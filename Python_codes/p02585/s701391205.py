# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
N, K = map(int, input().split())
Ps = list(map(int, input().split()))
Cs = list(map(int, input().split()))
max_list = list()
for i in range(N):
    next = Ps[i] - 1
    scores = [Cs[next]]
    while next != i:
        next = Ps[next] - 1
        scores.append(scores[-1] + Cs[next])
    l = len(scores)
    if K <= l:
        max_list.append(max(scores[:K]))
    else:
        if scores[-1] < 0:
            max_list.append(max(scores))
        else:
            a, b = divmod(K, l)
            cand1 = 0
            if b!=0:
                cand1 = a*scores[-1] + max(scores[:b])
            cand2 = (a-1)*scores[-1] + max(scores)
            max_list.append(max(cand1, cand2))
    #print(scores)
print(max(max_list))
