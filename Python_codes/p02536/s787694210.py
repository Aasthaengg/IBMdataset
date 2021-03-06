class UnionFindTree:
    """Union-Find Tree

    Attributes:
        n (int):    頂点数
        par (list): 要素の格納先
    """
    def __init__(self, n):
        """初期化 O(1)

        Args:
            n (int): 頂点数
        """
        self.par = [-1] * n

    def find(self, x):
        """要素の検索 O(α(N))

        Args:
            x (int): 対象要素

        Returns:
            int: xの根
        """
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]


    def union(self, x, y):
        """要素の併合 O(1)

        Args:
            x (int): 併合対象の集合に属する要素
            y (int): 併合対象の集合に属する要素
        """
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        """要素の判定 O(1)

        Args:
            x (int): 判定対象の要素
            y (int): 判定対象の要素

        Returns:
            bool: xとyが同じ集合に属するか否か
        """
        return self.find(x) == self.find(y)
    
    def size(self, x):
        """要素数の計算 O(1)

        Args:
            x (int): 対象要素

        Returns:
            int: xが属する集合の要素数
        """
        return -self.par[self.find(x)]


n, m = map(int, input().split())

uf = UnionFindTree(n)

for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

s = set()
for i in range(n):
    x = uf.find(i)
    if x not in s:
        s.add(x)

print(len(s) - 1)