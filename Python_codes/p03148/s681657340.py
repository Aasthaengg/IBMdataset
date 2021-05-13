# https://atcoder.jp/contests/abc116/submissions/5667980
# 写経

from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
kind_value = [[] for _ in range(n)]
for _ in range(n):
    t, d = map(int, input().split())
    kind_value[t - 1].append(d)

for lis in kind_value:
    lis.sort()

kind_value = sorted(
    (lis for lis in kind_value if lis),
    key=lambda x: x[-1], reverse=True)

ret = 0
curr = 0
kind = 0
remains = []
for lis in kind_value:
    kind += 1
    if kind > k:
        break
    curr += lis[-1]
    for d in lis[:-1]:
        heappush(remains, d)
        curr += d
    while len(remains) > k - kind:
        curr -= heappop(remains)
    ret = max(ret, curr + kind * kind)

print(ret)
