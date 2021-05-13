from collections import deque


class UnionFind:
    def __init__(self, v):
        self.v = v
        self._tree = list(range(v + 1))

    def _root(self, a):
        queue = deque()
        while self._tree[a] != a:
            queue.append(a)
            a = self._tree[a]
        while queue:
            index = queue.popleft()
            self._tree[index] = a
        return a

    def union(self, a, b):
        root_a = self._root(a)
        root_b = self._root(b)
        self._tree[root_b] = root_a

    def find(self, a, b):
        return self._root(a) == self._root(b)


N, M = map(int, input().split(' '))
edges = [tuple(map(int, input().split(' '))) for _ in range(M)]

bridges = 0
for a1, b1 in edges:
    union_find = UnionFind(N)
    for a2, b2 in edges:
        if a1 == a2 and b1 == b2:
            continue
        union_find.union(a2, b2)
    if not union_find.find(a1, b1):
        bridges += 1

print(bridges)
