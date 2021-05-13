H,W = map(int,input().split())
A = [input() for i in range(H)]
from collections import Counter
ctr = Counter()
for row in A:
    ctr.update(row)

if H%2==0 and W%2==0:
    print('Yes' if all(v%4==0 for v in ctr.values()) else 'No')
    exit()

odd = len([1 for v in ctr.values() if v%2])
pair = len([1 for v in ctr.values() if (v//2)%2==1])
if H%2 and W%2:
    if odd != 1:
        print('No')
    else:
        print('Yes' if pair <= H//2 + W//2 else 'No')
else:
    if odd:
        print('No')
    else:
        if H%2: H,W = W,H
        assert W%2
        print('Yes' if pair <= H//2 else 'No')