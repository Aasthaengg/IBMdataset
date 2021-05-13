import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')


N = int(input())

import collections
d = collections.defaultdict(int)

for _ in range(N):
    S = input()
    d[S] += 1

c = collections.Counter(d)
cnt = c.most_common()[0][-1]

a = []
for k, v in collections.Counter(d).most_common():
    if v != cnt:
        break
    a.append(k)

a.sort()
print(*a, sep="\n")