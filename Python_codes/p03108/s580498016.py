class UnionFind:
    __slots__ = ["_size", "_first_idx", "_parents"]

    def __init__(self, size: int, first_index: int = 0) -> None:
        self._size = size
        self._first_idx = first_index
        self._parents = [-1] * (size + first_index)

    def find(self, x: int) -> int:
        """Find the group (root) of vertex x"""
        if self._parents[x] < 0:
            return x
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def is_same(self, x: int, y: int) -> bool:
        """Return whether two vertices x and y are in the same group or not."""
        return self.find(x) == self.find(y)

    def unite(self, x: int, y: int) -> None:
        """Unite two groups of vertices x and y."""
        x, y = self.find(x), self.find(y)
        if x == y:
            return

        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x

    def get_size(self, x: int) -> int:
        """Get the size of the group vertex x belongs"""
        return -self._parents[self.find(x)]

    @property
    def groups(self) -> int:
        """Return the number of groups."""
        return len({self.find(x) for x in range(self._first_idx, self._size + self._first_idx)})
n,m=map(int,input().split())
ab=[]
for _ in range(m):
    ab.append(list(map(int,input().split())))
ab = ab[::-1]
tree=UnionFind(n)
ans = (n*(n-1)//2)
res=[ans]
for a,b in ab[:-1]:
    a -=1
    b -=1
    if tree.is_same(a,b):
        pass
    else:
        ans -= tree.get_size(a)*tree.get_size(b)
    res.append(ans)
    tree.unite(a,b)
print(*[max(0,i) for i in res[::-1]], sep="\n")