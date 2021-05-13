# from pprint import pprint
# import math
import collections

# n = int(input())
n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = [None] * m
c = [None] * m
for i in range(m):
    _b, _c = map(int, input().split(' '))
    b[i] = _b
    c[i] = _c

cnt = collections.Counter(a)

# カウンターのみ更新
for j in range(m):
    cnt.update({c[j]: b[j]})

a_tup = cnt.items()

# カウンターの結果を逆順にして合計n個になるまで取り出して加算
res = 0
num_cnt = 0
for _ in sorted(a_tup, reverse=True):
    res += _[0] * _[1]
    num_cnt += _[1]

    # n個を超えたらその分減らす
    if num_cnt >= n:
        res -= _[0] * (num_cnt - n)
        break

print(res)
