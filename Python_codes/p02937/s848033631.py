import sys
from collections import defaultdict
import bisect
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

S = sr()
T = sr()
len_S = len(S)
indexes_S = defaultdict(list)
for i, s in enumerate(S):
    indexes_S[s].append(i)

x = -1 # 今いるところ、次はx+1から探索
for t in T:
    if len(indexes_S[t]) == 0:
        print(-1); exit()
    arr = indexes_S[t]
    y = (x+1) % len_S
    next_i = bisect.bisect_left(arr, y) # tの同じ文字がある次のindex
    if next_i < len(arr):
        x = (x+1) + arr[next_i] - y
    else:
        x = (x+1) + arr[0] + len_S - y # 1周して次のarr

print(x+1)
