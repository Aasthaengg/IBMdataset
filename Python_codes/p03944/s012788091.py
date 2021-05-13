import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

W, H, N = map(int, input().split())

lx = 0
rx = W
by = 0
ty = H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        lx = max(lx, x)
    if a == 2:
        rx = min(rx, x)
    if a == 3:
        by = max(by, y)
    if a == 4:
        ty = min(ty, y)
if rx - lx < 0 or ty - by < 0:
    print(0)
else:
    s = (rx - lx) * (ty - by)
    print(s)