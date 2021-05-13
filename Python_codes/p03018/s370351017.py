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

s = input()
s = s.replace('BC', 'D')
s_list = s.split("B")
x = []
for e in s_list:
    x += e.split("C")

ans = 0
for e in x:
    cnt_d = 0
    now = 0
    for c in e[::-1]:
        if c == 'D':
            cnt_d += 1
        if c == 'A':
            now += cnt_d
    ans += now
print(ans)
        

