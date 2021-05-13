# # -*- coding: utf-8 -*-
X, Y, A, B, C = map(int, input().split(' '))
P = list(map(int, input().split(' ')))
Q = list(map(int, input().split(' ')))
R = list(map(int, input().split(' ')))

apples = []
apples.extend([(p, 0) for p in P])
apples.extend([(q, 1) for q in Q])
apples.extend([(r, 2) for r in R])
apples.sort(key=lambda x: x[0], reverse=True)

ans = 0
num = X + Y
thresholds = [X, Y, C]
for v, category in apples:
    # もうその色のリンゴを取れない
    if not thresholds[category]:
        continue

    num -= 1
    thresholds[category] -= 1
    ans += v

    if num == 0:
        break

print(ans)


