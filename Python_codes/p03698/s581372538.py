# -*- coding: utf-8 -*-
import sys
from collections import defaultdict, deque
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1]


def solve():
    s = input()
    w = set()
    for e in s:
        if e in w:
            print('no')
            return
        w.add(e)
    print("yes")

        
t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()



"""

1 4
7
RRRR
1 1 0 1
----
4

1 4
47
RCRR
1 1 0 1
----
-1

2 2
10
RR
RR
1 7
4 1
----
4

2 2
10
RR
RR
7 4
7 4
----
-1

3 3
8
RCR
RRC
RRR
1 1 1
1 1 1
1 3 1


3 3
1
RCR
RRC
RRR
1 1 1
1 1 1
1 3 1


"""



