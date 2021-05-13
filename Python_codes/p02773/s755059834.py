N=int(input())
l=[input() for _ in range(N)]

l= sorted(l)

import collections
c = collections.Counter(l)
d = c.most_common()

for i in range(len(d)):
    if d[i][1] == d[0][1]:
        print(d[i][0])