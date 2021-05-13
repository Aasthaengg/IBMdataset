from pprint import pprint
 
# import math
# import collections
 
n = int(input())
# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
t, x, y = [0], [0], [0]
d = [0]
dd = [0]
td = [0]
 
for i in range(1, n + 1):
    _t, _x, _y = map(int, input().split(' '))
    t.append(_t)
    x.append(_x)
    y.append(_y)
 
    d.append(abs(x[i] - x[0]) + abs(y[i] - y[0]))
    dd.append(abs(x[i] - x[i-1]) + abs(y[i] - y[i-1]))
    td.append(t[i] - t[i-1])
 
# 時刻の奇遇と距離の奇遇は一致する
# d <= t である
movable = [False] * (n + 1)
 
for i in range(n + 1):
    if d[i] <= t[i] and (t[i] % 2 == d[i] % 2) and dd[i] <= td[i]:
        movable[i] = True
 
if all(movable):
    res = 'Yes'
else:
    res = 'No'
 
# pprint(d)
# pprint(movable)
print(res)