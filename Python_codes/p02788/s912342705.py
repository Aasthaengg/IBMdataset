import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

import math
from collections import deque
    
n,d,a = l_in()
xh = []
for _ in range(n):
    x,h=l_in()
    xh.append((x,math.ceil(h/a)))

xh.sort()
res = 0
currentX = -1
currentH = 0
q=deque()
q_sum = 0

for x,h in xh:
    while len(q) > 0:
        bx, bh = q[0]
        if bx < x:
            q.popleft()
            q_sum -= bh
        else:
            break
    h -= q_sum
    if h > 0:
        q.append((x+2*d, h))
        q_sum += h
        res += h

print(res)

