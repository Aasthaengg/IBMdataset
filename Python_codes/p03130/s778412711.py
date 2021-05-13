a = []
b = []
for i in range(3):
    x1,y1=[int(i) for i in input().split()]
    a.append(x1)
    b.append(y1)

path=a+b

import collections
c=collections.Counter(path)

values,counts =zip(*c.most_common())

if counts==(2,2,1,1):
    print('YES')
else:
    print('NO')