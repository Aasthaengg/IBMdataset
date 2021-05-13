# -*- coding: utf-8 -*-
N, K = map(int, input().split(' '))
points = [list(map(int, input().split(' '))) for i in range(N)]

X = list(set([x for x, y in points]))
Y = list(set([y for x, y in points]))

X.sort()
Y.sort()

ans = float('inf')
for i, min_x in enumerate(X):
    for max_x in X[i+1:]:
        for j, min_y in enumerate(Y):
            for max_y in Y[j + 1:]:
                m = (max_x - min_x) * (max_y - min_y)
                internal_points = [(x, y) for x, y in points if min_x <= x <= max_x and min_y <= y <= max_y]
                if len(internal_points) >= K:
                    ans = min(ans, m)

print(ans)