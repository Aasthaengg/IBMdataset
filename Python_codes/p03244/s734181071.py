from collections import Counter

n = int(input())
v = [int(x) for x in input().split()]

v1 = Counter(v[0::2]).most_common() + [(0, 0)]
v2 = Counter(v[1::2]).most_common() + [(0, 0)]

if v1[0][0] != v2[0][0]:
    res = n - v1[0][1] - v2[0][1]
else:
    res = min(n - v1[0][1] - v2[1][1], n - v1[1][1] - v2[0][1])

print(res)
