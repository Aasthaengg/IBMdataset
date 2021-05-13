H,W = map(int,input().split())
A = [input() for i in range(H)]
from collections import Counter
ctr = Counter()
for row in A:
    ctr.update(row)

if H%2==0 and W%2==0:
    print('Yes' if all(v%4==0 for v in ctr.values()) else 'No')
    exit()

if H%2==0 or W%2==0:
    if H%2: H,W = W,H
    if any(v%2 for v in ctr.values()):
        print('No')
        exit()
    pair = 0
    for v in ctr.values():
        if v%4==2:
            pair += 1
    print('Yes' if pair*2 <= H else 'No')

else:
    odd = 0
    for k in ctr.keys():
        if ctr[k]%2:
            odd += 1
            ctr[k] -= 1
    if odd != 1:
        print('No')
        exit()
    pair = 0
    for v in ctr.values():
        if v%4==2:
            pair += 1
    print('Yes' if pair*2 <= H+W-2 else 'No')