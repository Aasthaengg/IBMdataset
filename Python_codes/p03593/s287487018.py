from collections import defaultdict
h, w = map(int, input().split())

cnt = defaultdict(int)
for _ in range(h):
    for a in input():
        cnt[a] += 1

quartet = (h//2) * (w//2)
doublet = (h % 2)*(w//2)+(w % 2)*(h//2)
singlet = 1 if h & 1 and w & 1 else 0

for k, v in cnt.items():
    if not quartet:
        break
    if v < 4:
        continue
    x = min(quartet, v//4)
    quartet -= x
    cnt[k] -= 4*x

for k, v in cnt.items():
    if v < 2:
        continue
    doublet -= v//2
    cnt[k] = v % 2

singlet -= sum(v for v in cnt.values())
if singlet == doublet == quartet == 0:
    print('Yes')
else:
    print('No')
