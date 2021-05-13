import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import Counter

n, k, *a = map(int, read().split())
c = Counter(a)

l = list(c.items())
l.sort(key=lambda x: x[1])

ans = 0
for i in range(len(set(a)) - k):
    ans += l[i][1]
print(ans)