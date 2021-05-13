import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import defaultdict
mod = 10**9+7

N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
cnt = defaultdict(int)
for i in range(N):
    for j in range(i+1, N):
        a, b = xy[j][0]-xy[i][0], xy[j][1]-xy[i][1]
        cnt[(a, b)] += 1
        cnt[(-a, -b)] += 1
if N == 1:
    print(1)
else:
    print(N-max(cnt.values()))
