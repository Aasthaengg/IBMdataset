from collections import Counter
H, W = map(int, input().split())
counter = Counter()
for h in range(H):
    row = input()
    for a in row:
        counter[a] += 1
ans = True
if (H * W) % 2 == 0:
    for k, v in counter.items():
        if v % 2 == 0:
            continue
        ans = False
        break
    
else:
    odd_count = 0
    for k, v in counter.items():
        if v % 2 == 0:
            continue
        odd_count += 1
    if odd_count != 1:
        ans = False
if ans:
    g3 = (H // 2) * (W // 2)
    for k, v in counter.items():
        if v >= 4:
            g3 -= v // 4
    if g3 <= 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')