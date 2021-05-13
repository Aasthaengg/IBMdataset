__DEUBG__ = 0

import math
import sys

num = int(input())
seq = list(map(int, input().split()))

prev = None
tmp = []
increase = None
count = 0

def dump(x):
    from pprint import pprint
    pprint(x)

#breakpoint()

for x in seq:
    if __DEUBG__:
        print(x)
        print(tmp)
    if prev is None:
        tmp = [x]
    elif increase is True:
        if x >= tmp[-1]:
            tmp.append(x)
        else:
            if __DEUBG__:
                dump(tmp)
            tmp = [x]
            increase = None
            count += 1
    elif increase is False:
        if x <= tmp[-1]:
            tmp.append(x)
        else:
            if __DEUBG__:
                dump(tmp)
            tmp = [x]
            increase = None
            count += 1
    elif increase is None:
        if x == tmp[-1]:
            pass
        elif x > tmp[-1]:
            increase = True
        else:
            increase = False
        tmp.append(x)
    prev = x

if __DEUBG__:
    dump(tmp)

count += 1
print(count)
