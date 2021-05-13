# -*- coding: utf-8 -*-


#
import collections
H, W, N = map(int, input().split(' '))

point_frq_dict = collections.defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split(' '))
    for i in range(3):
        for j in range(3):
            if 0 < a-i < H-1 and 0 < b-j < W-1:
                point_frq_dict[(a-i, b-j)] += 1

ans = [0 for _ in range(10)]
n = 0
for frq in point_frq_dict.values():
    ans[frq] += 1

ans[0] = (H-2)*(W-2) - sum(ans)
for a in ans:
    print(a)

