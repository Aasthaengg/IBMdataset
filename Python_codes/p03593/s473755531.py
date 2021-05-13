from collections import defaultdict
H, W = map(int, input().split())
a = [input() for i in range(H)]
C = defaultdict(int)
for s in a:
    for c in s:
        C[c] += 1
m = [0]*4
for k in C:
    m[C[k]%4] += 1
if H&1 and W&1:
    if m[1]+m[3] == 1 and m[2] <= H//2+W//2-m[3]:
        print('Yes')
    else:
        print('No')
elif H&1==0 and W&1==0:
    if all([C[x]%4==0 for x in C]):
        print('Yes')
    else:
        print('No')
else:
    if H&1:
        H, W = W, H
    if m[1] == m[3] == 0 and m[2] <= H//2:
        print('Yes')
    else:
        print('No')