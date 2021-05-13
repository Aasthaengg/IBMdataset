# import math
# import collections
# from pprint import pprint

# n = int(input())
n, m = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
a = []
for i in range(n):
    a.append(list(input()))
b = []
for i in range(m):
    b.append(list(input()))

judge = False
for offset_i in range(n - m + 1):
    for offset_j in range(n - m + 1):

        flg = 0
        for i in range(m):
            for j in range(m):
                if a[i + offset_i][j + offset_j] == b[i][j]:
                    flg += 1

        if flg == m * m:
            judge = True
            # print('find', offset_i, offset_j)

if judge:
    print('Yes')
else:
    print('No')
