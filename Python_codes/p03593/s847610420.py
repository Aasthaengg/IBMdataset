# -*- coding: utf-8 -*-
import collections

H, W = map(int, input().split())
a_frq_dict = collections.defaultdict(int)
for _ in range(H):
    for a in input():
        a_frq_dict[a] += 1


n = H%2 + W%2
frq1, frq2, frq4 = 0,0,0

if n == 2:
    frq1 = 1
    frq2 = (H-1)//2 + (W-1)//2
    frq4 = ((H*W) - (frq2*2 + frq1)) // 4

elif n == 1:
    if H%2:
        frq2 = W//2
    else:
        frq2 = H//2

    frq4 = ((H*W) - frq2*2) // 4

else:
    frq4 = (H * W) // 4


# print(frq1, frq2, frq4)


for frq in a_frq_dict.values():
    n = min(frq4, frq//4)
    frq4 -= n
    frq -= n*4

    n = min(frq2, frq//2)
    frq2 -= n
    frq -= n*2

    n = min(frq1, frq)
    frq1 -= n
    frq -= n

    # print(frq)

    if frq:
        print('No')
        exit()


# print(frq1, frq2, frq4)

if all(map(lambda x: x == 0, [frq1, frq2, frq4])):
    print('Yes')
else:
    print('No')




