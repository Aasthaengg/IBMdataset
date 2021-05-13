import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.buffer.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

n = ri()
l = len(str(n)) - 1
if n % 10**l == 0:
    if str(n)[0] == '1':
        print(10)
    else:
        ans = 0
        for i in str(n):
            ans += int(i)
        print(ans) 
else:
    ans = 0
    for i in str(n):
        ans += int(i)
    print(ans)

