import collections
ls = list(map(int,input().split()))
counter = collections.Counter(ls)
ls2 = list(counter.values())
if 2 in ls2:
    print('Yes')
else:
    print('No')