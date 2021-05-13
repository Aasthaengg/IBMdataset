import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import defaultdict


N = int(read())
counter = defaultdict(int)
for x in map(str,range(1,N+1)):
    head = x[0]
    tail = x[-1]
    counter[(head, tail)] += 1
ans = 0
items = list(counter.items())
for (head, tail), cnt in items:
    ans += cnt * counter[(tail, head)]
print(ans)
