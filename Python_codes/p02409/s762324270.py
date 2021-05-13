# coding=utf-8
from copy import deepcopy

rooms = dict(zip(range(1, 11), [0] * 10))
building = dict(zip(range(1, 4), [deepcopy(r) for r in [rooms]*3]))
buildings = dict(zip(range(1, 5), [deepcopy(b) for b in [building]*4]))

# input
n = input()
for _ in xrange(n):
    b, f, r, v = map(int, raw_input().split())
    buildings[b][f][r] += v

# print result
for b in range(1, 5):
    for f in range(1, 4):
        rooms = buildings[b][f]
        print ' ' + ' '.join(map(str, [rooms[i] for i in xrange(1, 11)]))
    if b != 4:
        print '#' * 20