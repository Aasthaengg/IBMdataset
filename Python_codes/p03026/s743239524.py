#!/usr/bin/env python
from collections import defaultdict

N = int(input())

ab = []
for _ in range(N - 1):
    ab.append(tuple(map(int, input().split())))
c = sorted(list(map(int, input().split())), reverse=True)

nodes = defaultdict(set)
for a, b in ab:
    nodes[a].add(b)
    nodes[b].add(a)

d = {}
done = set()
stack = [1]
ci = 0
node = 1
while stack:
    node = stack.pop()
    d[node] = c[ci]
    stack += list(nodes[node] - done)
    done.add(node)
    ci += 1

print(sum(c[1:]))
for i in range(N):
    print(d[i + 1], end=' ')
print()

