import collections
l = list(map(int, input().split()))
c = collections.Counter(l)
values, counts = zip(*c.most_common())
if counts[0] == 2:
    print('Yes')
else:
    print('No')