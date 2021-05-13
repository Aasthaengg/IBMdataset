n = int(input())
v = list(map(int,input().split()))

v1 = v[::2]
v2 = v[1::2]

from collections import Counter

v1c = Counter(v1).most_common()
v2c = Counter(v2).most_common()

v1c.append([0,0])
v2c.append([0,0])

if v1c[0][0] == v2c[0][0]:
    ans = max(v1c[0][1] + v2c[1][1], v1c[1][1] + v2c[0][1])
else:
    ans = v1c[0][1] + v2c[0][1]

print(n-ans)
