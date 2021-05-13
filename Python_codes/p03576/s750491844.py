
import itertools as it

from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())



N, K = acinput()


ary = [acinput() for i in range(N)]
x = list(map(lambda x: x[0], sorted(ary, key=lambda s: s[0])))
y = list(map(lambda x: x[1], sorted(ary, key=lambda x: x[1])))


#print(list(it.combinations(y,2)))
#print(list(x))

res = 10**20
for sy in it.combinations(y, 2):
    #print(sy)
    for sx in it.combinations(x, 2):
        #print(sx)
        #print(sy, sx)
        count = 0
        for sa in ary:
            
            if sy[0] <= sa[1] and sa[1] <= sy[1]:
                if sx[0] <= sa[0] and sa[0] <= sx[1]:
                    count += 1

        #print(count)
        if count >= K:
            #dx = np.diff(sx)[0]
            #dy = np.diff(sy)[0]
            dx=sx[1]-sx[0]
            dy=sy[1]-sy[0]
            #print(dx,dy)
            res = min(res, dx*dy)
            #print(res)

print(res)

