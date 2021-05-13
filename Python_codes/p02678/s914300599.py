import sys
input = sys.stdin.readline
from collections import defaultdict, deque

(n, m), g = map(int, input().split()), defaultdict(list)
for i in range(m): a, b = map(int, input().split()); g[a].append(b); g[b].append(a)
s, q = [0, 0] + [-1 for i in range(1, n)], deque([1])
for i in range(2, n + 1):
    x = q.popleft()
    for a in g[x]:
        if s[a] == -1: q.append(a); s[a] = x
if not all([a != -1 for a in s]): print('No')
else:
    print('Yes')
    for i in s[2:]: print(i)