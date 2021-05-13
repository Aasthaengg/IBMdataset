import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import Counter

n, *a = map(int, read().split())

c = Counter(a)
ans =0
for k, v in c.items():
    if v >= k:
        ans += v - k
    elif v < k:
        ans += v
print(ans)
