import sys
from collections import Counter
h, w = [int(i) for i in sys.stdin.readline().split()]
a_ls = []
ct = Counter()
for y in range(h):
    a = [i for i in sys.stdin.readline().strip()]
    a_ls.append(a)
    ct.update(a)
g1 = h % 2 & w % 2
g2 = (h // 2) * (w % 2) + (w // 2) * (h % 2)
g4 = (h // 2) * (w // 2)
cnt = 0
for c in ct.keys():
    if cnt == g1:
        break
    if ct[c] % 2 == 1:
        ct[c] -= 1
        cnt += 1
cnt = 0
for c in ct.keys():
    if cnt == g2:
        break
    if ct[c] % 4 == 2:
        ct[c] -= 2
        cnt += 1
if all([ct[c] % 4 == 0 for c in ct.keys()]):
    print("Yes")
else:
    print("No")