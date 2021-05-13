#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
 
h, w, n = [int(item) for item in input().split()]
blk_cnt = defaultdict(int) 
 
for i in range(n):
    a, b = [int(item) - 1 for item in input().split()]
    for j in range(-1, 2):
        for k in range(-1, 2):
            blk_cnt[(a + j, b + k)] += 1
ans = [0] * 10 
for key in blk_cnt.keys():
    if key[0] < 1 or key[1] < 1 or key[0] >= h-1 or key[1] >= w-1:
        continue
    ans[blk_cnt[key]] += 1
total = (w - 2) * (h - 2)
ans[0] = total - sum(ans)
for item in ans:
    print(item)