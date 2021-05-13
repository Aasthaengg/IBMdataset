import sys
from collections import defaultdict
from itertools import groupby

read = sys.stdin.read

N, *C = map(int, read().split())
C = [i for i, _ in groupby(C)]
mod = 10 ** 9 + 7
cnt = defaultdict(int)
dp = 1
for i in C:
    prev = dp
    dp = (cnt[i] + dp) % mod
    cnt[i] = (cnt[i] + prev) % mod

print(dp)
