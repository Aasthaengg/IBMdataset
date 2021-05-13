from collections import Counter
from functools import reduce
from operator import add

h, w = map(int, input().split())
a_counts = [Counter(input()) for _ in range(h)]
counts = reduce(add, a_counts)

if h%2==0 and w%2==0:
    if all([x%4==0 for x in counts.values()]):
        print('Yes')
        exit()
    else:
        print('No')
        exit()
elif h%2==0 and w%2==1:
    mod4 = [x%4 for x in counts.values()]
    mod2 = [x%2 for x in mod4 if x!=0]

    if all([x==0 for x in mod2]) and len(mod2) <= h//2:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
elif h%2==1 and w%2==0:
    mod4 = [x%4 for x in counts.values()]
    mod2 = [x%2 for x in mod4 if x!=0]

    if all([x==0 for x in mod2]) and len(mod2) <= w//2:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
else:
    mod4 = [x%4 for x in counts.values()]
    mod2 = [x%2 for x in mod4 if x!=0]
    mod2_0 = [x for x in mod2 if x==0]
    mod2_1 = [x for x in mod2 if x==1]

    if len(mod2_0) <= w//2 + h//2 and len(mod2_1) <= 1:
        print('Yes')
        exit()
    else:
        print('No')
        exit()