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

N = int(input())
ans = 0

end_a = 0
start_b = 0
both = 0
for i in range(N):
    S = input()
    ans += S.count("AB")
    if S[-1] == 'A' and S[0] == 'B':
        both += 1
    elif S[-1] == 'A':
        end_a += 1
    elif S[0] == 'B':
        start_b += 1

if both == 0:
    ans += min(start_b, end_a)
else:
    if start_b + end_a > 0:
        ans += both + min(start_b, end_a)
    else:
        ans += both - 1
# if end_a > start_b:
#     ans += start_b
#     end_a -= start_b
#     start_b = 0
# else:
#     ans += end_a
#     start_b -= end_a
#     end_a = 0

# if both >= 1:
#     ans += both - 1
#     if start_b > 0:
#         ans += 1
#     if end_a > 0:
#         ans += 1
print(ans)

