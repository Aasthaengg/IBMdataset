# -*- coding: utf-8 -*-
N = int(input())

if N == 1:
    print(1)
    exit()

#
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split(' '))
    X.append(x)
    Y.append(y)

#
import collections
xy_frq_dict = collections.defaultdict(int)
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        x, y = X[i] - X[j], Y[i] - Y[j]
        xy_frq_dict[(x, y)] += 1

xy_frq_pairs = list(xy_frq_dict.items())
xy_frq_pairs.sort(key=lambda x: x[1])
ret = N - xy_frq_pairs[-1][1]
print(ret)



