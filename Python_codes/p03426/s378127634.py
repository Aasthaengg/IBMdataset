# -*- coding: utf-8 -*-
H, W, D = map(int, input().split(' '))
n_position_dict = {}

for h in range(H):
    A = list(map(int, input().split(' ')))
    for w in range(W):
        n_position_dict[A[w]] = (h, w)

diffs = [1 for _ in range(H*W+1)]
for i in range(D+1, H*W+1):
    h, w = n_position_dict[i]
    next_h, next_w = n_position_dict[i-D]
    diffs[i] = diffs[i-D] + abs(h - next_h) + abs(w - next_w)
# print(diffs)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split(' '))
    ret = diffs[r] - diffs[l]
    print(ret)







