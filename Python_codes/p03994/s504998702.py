import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
S = input()
K = int(input())

ans = []
for i, c in enumerate(S):
    if c == 'a':
        ans.append(c)
        continue
    num = ord('z') - ord(c) + 1
    if K >= num:
        K -= num
        ans.append('a')
    else:
        ans.append(c)
if K > 0:
    ans[-1] = chr((ord(ans[-1]) - ord('a') + K % 26) % 26 + ord('a'))
print("".join(ans))
    
