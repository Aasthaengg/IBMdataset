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
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N, K = map(int, input().split())
A = list(sorted(map(int, input().split())))
s = sum(A)
i = 2
cands = [s]
while i ** 2 <= s:
    if s % i == 0:
        cands.append(i)
        cands.append(s // i)
    i += 1
cands = sorted(cands)

ans = 1
for cand in cands:
    B = deque(list(sorted(map(lambda x: x % cand, A), reverse=True)))
    k = 0
    while len(B) > 0:
        x = B.popleft()
        while x % cand != 0:
            y = B.pop()
            z = x + y
            if z > cand:
                k += cand - x
                x = cand
                y = z - cand
                B.append(y)
            else:
                k += y
                x = z
    if k <= K:
        ans = max(ans, cand)
print(ans)