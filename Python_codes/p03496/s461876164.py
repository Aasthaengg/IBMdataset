# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split(' ')))

#
max_a = max(a)
min_a = min(a)
sign = lambda x: 1 if x >= 0 else -1

ans = []

if sign(max_a) == sign(min_a):
    # 全ての正負が同じ
    if max_a > 0:
        for j in range(N-1):
            ans.append((j, j+1))

    else:
        for j in range(N-1, 0, -1):
            ans.append((j, j-1))


else:
    # 全ての正が異なる
    if abs(max_a) >= abs(min_a):
        # 正の方が大きい
        i = a.index(max_a)
        for j in range(N):
            if i != j:
                ans.append((i, j))

        for j in range(N-1):
            ans.append((j, j+1))


    else:
        # 負の方が大きい
        i = a.index(min_a)
        for j in range(N):
            if i != j:
                ans.append((i, j))

        for j in range(N-1, 0, -1):
            ans.append((j, j-1))

print(len(ans))
for i, j in ans:
    print(i+1, j+1)


