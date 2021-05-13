#!/usr/bin/env python3
#ディスカバリーチャンネルコードコンテスト2020 A

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))


x,y = LI()
if x == 3 and y == 3:
    print(200000)
elif x == 2 and y == 2:
    print(400000)
elif (x == 1 and y == 2) or (x == 2 and y == 1):
    print(500000)
elif (x == 3 and y == 2) or (x == 2 and y == 3):
    print(300000)
elif (x == 3 and y == 1) or (x == 1 and y == 3):
    print(400000)
elif x == 1 and y == 1:
    print(600000+400000)
elif x == 3 or y == 3:
    print(100000)
elif x == 2 or y == 2:
    print(200000)
elif x == 1 or y == 1:
    print(300000)
else:
    print(0)