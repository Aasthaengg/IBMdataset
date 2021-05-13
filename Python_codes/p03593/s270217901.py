# coding: utf-8
from collections import defaultdict
import sys

H, W = (int(x) for x in input().split())

freq = defaultdict(int)

for i in range(H):
    for c in input():
        freq[c] += 1

nDiv4 = 0
nDiv2 = 0
nDiv1 = 0
for c in freq:
    num = freq[c]

    d4 = num // 4
    nDiv4 += d4
    num -= d4 * 4

    d2 = num // 2
    nDiv2 += d2
    num -= d2 * 2

    nDiv1 += num 

canDiv2 = 0
if H % 2 != 0:
    canDiv2 += W // 2
if W % 2 != 0:
    canDiv2 += H // 2

if H % 2 != 0 and W % 2 != 0:
    if nDiv1 != 1:
        print("No")
        sys.exit(0)
else:
    if nDiv1 != 0:
        print("No")
        sys.exit(0)

if nDiv2 <= canDiv2:
    print("Yes")
else:
    print("No")

#print(nDiv1, nDiv2, nDiv4)
#print(nDiv2, canDiv2)