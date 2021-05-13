H,W = map(int,input().split())
A = [input() for i in range(H)]
from collections import Counter
ctr = Counter()
for row in A:
    ctr.update(row)

if H%2==0 and W%2==0:
    print('Yes' if all(v%4==0 for v in ctr.values()) else 'No')
elif H%2 and W%2:
    odd = 0
    for k,v in ctr.items():
        if v%2:
            odd += 1
            ctr[k] -= 1
    if odd != 1:
        print('No')
        exit()
    four = 0
    for v in ctr.values():
        four += (v//4)*4
    want = (H-H%2)*(W-W%2)
    print('Yes' if four >= want else 'No')
else:
    if any(v%2 for v in ctr.values()):
        print('No')
        exit()
    four = 0
    for v in ctr.values():
        four += (v//4)*4
    want = (H-H%2)*(W-W%2)
    print('Yes' if four >= want else 'No')