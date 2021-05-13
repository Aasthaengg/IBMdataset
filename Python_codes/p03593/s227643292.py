from collections import Counter

h, w = map(int, input().split())
ctr = Counter()
for _ in range(h):
    ctr.update(input())

need = [0] * 3  # need[x]:=2**x個重複している要素の必要数
if h % 2 == 0:
    if w % 2 == 0:
        need[2] = h * w
    else:
        need[2] = h * w - h
        need[1] = h
else:
    if w % 2 == 0:
        need[2] = h * w - w
        need[1] = w
    else:
        need[2] = h * w - (h + w - 1)
        need[1] = h + w - 2
        need[0] = 1

for power in range(2, -1, -1):
    for char in ctr:
        if not need[power]:
            break
        p2 = pow(2, power)
        while ctr[char] >= p2:
            ctr[char] -= p2
            need[power] -= p2

if any(p > 0 for p in need):
    print('No')
else:
    print('Yes')

# ee
# 4: h*w

# eo, even=h
# 2: h
# 4: h*w - h

# oo
# 1: 1
# 2: h+w-1
# 4: h*w-(h+w)
