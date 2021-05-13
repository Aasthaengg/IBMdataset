import collections
s = str(input())

c = list(collections.Counter(s).values())
c.sort(reverse=True)

#print(c)
if len(c) <= 2:
    if c[0] >= 2:
        print('NO')
    else:
        print('YES')

else:
    if abs(c[0]-c[1]) >= 2 or abs(c[1]-c[2]) >= 2 or abs(c[2]-c[0]) >= 2:
        print('NO')
    else:
        print('YES')

