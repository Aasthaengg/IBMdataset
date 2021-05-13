from pprint import pprint

# import math
# import collections

# n = int(input())
# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))

c = []
for i in range(3):
    c.append(list(map(int, input().split(' '))))

diff_v = [[0] * 3 for i in range(3)]
diff_h = [[0] * 3 for i in range(3)]

for i in range(0, 3):
    for j in range(0, 3):
        if i > 0:
            diff_v[i][j] = c[i][j] - c[i - 1][j]

for j in range(0, 3):
    for i in range(0, 3):
        if j > 0:
            diff_h[j][i] = c[i][j] - c[i][j - 1]


def map_all(es):
    return all([e == es[0] for e in es[1:]]) if es else False


eq_v = all([map_all(d) for d in diff_v])
eq_h = all([map_all(d) for d in diff_h])

if eq_v and eq_h:
    print('Yes')
else:
    print('No')
