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

N, M, K = map(int, input().split())
ok = False
for i in range(N + 1):
    # now = M * i
    for j in range(M + 1):
        now = i * (M - j) + (N - i) * j
        if now == K:
            ok = True
        # now -= j * i
        # now += j * (N - i)
        # if now == K:
        #     ok = True
if ok:
    print("Yes")
else:
    print("No")