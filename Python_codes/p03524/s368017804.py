import collections
s = list(input())
tmp = len(set(s))
c = collections.Counter(s).most_common()
if (c[0][1] >= c[-1][1] + 2 and tmp == 3) or (tmp == 2 and len(s) > 2) or (tmp == 1 and len(s) != 1):
    print('NO')
else:
    print('YES')
