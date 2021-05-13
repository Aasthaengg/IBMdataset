import numpy as np

n = int(input())
ab = []

for _ in range(n):
    ab.append(list(map(int, input().split())))

a = np.array([x[0] for x in ab])
b = np.array([x[1] for x in ab])


ans = 0
for x, y in zip(a[::-1], b[::-1]):
    mod = (x + ans) % y
    if mod == 0:
        continue
    else:
        add = y - mod
        ans += add

print(ans)