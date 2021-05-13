import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = defaultdict(int)
cnt[0] = 1
acc = 0
ans = 0

for Ai in A:
    acc += Ai
    ans += cnt[acc%M]
    cnt[acc%M] += 1

print(ans)