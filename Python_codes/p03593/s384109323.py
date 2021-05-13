import sys
from collections import Counter
read = sys.stdin.read
readline = sys.stdin.readline

H, W = map(int, readline().split())
a = read().split()
s = []
for i in a:
    s.extend(list(i))

s = Counter(s)
r = [0] * 4
for i in s.values():
    r[i % 4] += 1

if r[1] + r[3] > 1:
    print('No')
    exit()

h = H % 2
w = W % 2

if h and w:
    if not r[1]:
        r[3] -= 1
        r[2] += 1
    if H + W - r[2] * 2 >= 0 and (H + W - 2 - r[2] * 2) % 4 == 0:
        print('Yes')
    else:
        print('No')
else:
    if r[1] + r[3] != 0:
        print('No')
        exit()
    if h:
        if W - r[2] * 2 >= 0 and (W - r[2] * 2) % 4 == 0:
            print('Yes')
        else:
            print('No')
    elif w:
        if H - r[2] * 2 >= 0 and (H - r[2] * 2) % 4 == 0:
            print('Yes')
        else:
            print('No')
    else:
        if r[0] and r.count(0) == 3:
            print('Yes')
        else:
            print('No')