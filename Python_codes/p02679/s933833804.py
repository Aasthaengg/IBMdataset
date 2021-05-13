import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
N = int(input())
MOD = 10**9+7
AB = []
x = 0
y = 0
d = defaultdict(int)
ch = defaultdict(int)
flag = 0
for _ in range(N):
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        flag += 1
    elif a == 0:
        d[(0,1)] += 1
        AB.append([0,1])
    elif b == 0:
        d[(1,0)] += 1
        AB.append([1,0])
    else:
        dd = math.gcd(abs(a),abs(b))
        a //= dd
        b //= dd
        if a < 0:
            a *= -1
            b *= -1
        d[(a,b)] += 1
        AB.append([a,b])
n = len(AB)
ans = 1
if n > 0:
  for i in range(n):
      a,b = AB[i]
      if ch[(a,b)] == 1:
          continue
      m = d[(a,b)]
      if b > 0:
          l = d[(b,(-1)*a)]
          ch[(a,b)] = 1
          ch[(b,(-1)*a)] = 1
      elif a == 0 or b == 0:
          l = d[(b,a)]
          ch[(a,b)] = 1
          ch[(b,a)] = 1
      else:
          l = d[((-1)*b,a)]
          ch[(a,b)] = 1
          ch[((-1)*b,a)] = 1
      ans *= (pow(2,m,MOD)+pow(2,l,MOD)-1)
      ans = ans % MOD
ans = ans % MOD
ans = ans -1 + flag
ans = ans % MOD
print(ans)
