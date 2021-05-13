from collections import Counter

N = int(input())
V = tuple(map(int, input().split(' ')))

v1 = V[::2]
v2 = V[1::2]

v1_count = Counter(v1)
v1_count[-1] = 0
v2_count = Counter(v2)
v2_count[-1] = 0

v1 = sorted([(value, key) for key, value in v1_count.items()], reverse=True)
v2 = sorted([(value, key) for key, value in v2_count.items()], reverse=True)

if v1[0][1] == v2[0][1]:
    print(min(N - v1[0][0] - v2[1][0], N - v2[0][0] - v1[1][0]))
else:
    print(N - v1[0][0] - v2[0][0])
