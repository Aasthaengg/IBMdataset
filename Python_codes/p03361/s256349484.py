# from pprint import pprint
# import math
# import collections

# n = int(input())
h, w = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
s = []
for i in range(h):
    s.append(list(input()))

# すべての黒マスについて、上下左右に隣接している黒マスがあるかどうかを調べてあればOK
check = [[None] * w for i in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            check[i][j] = False
            if i > 0 and s[i - 1][j] == '#':
                check[i][j] = True

            if i < h - 1 and s[i + 1][j] == '#':
                check[i][j] = True

            if j > 0 and s[i][j - 1] == '#':
                check[i][j] = True

            if j < w - 1 and s[i][j + 1] == '#':
                check[i][j] = True
        else:
            check[i][j] = True

if all([all(c) for c in check]):
    print('Yes')
else:
    print('No')
