# -*- coding: utf-8 -*-
# C - Base -2 Number
import sys 
from collections import defaultdict
from itertools import accumulate
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,M = map(int,readline().split())
A = list(map(int,readline().split()))
S = list(accumulate(A))
d = defaultdict(int)
for i in range(N):
    a = S[i] % M
    d[a] += 1
ans = d[0]
for n in d.values():
    ans += (n-1)*n // 2
print(ans)