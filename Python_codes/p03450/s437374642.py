class WeightedUnionFindTree:
    """Disjoint-Set Data Structure with weight

    complexity:
        - init: O(n)
        - find, unite, same: O(alpha(n))
    """

    def __init__(self, n_nodes):
        self.par = [i for i in range(n_nodes)]  # parent
        self.rank = [0] * n_nodes  # depth of tree
        self.weights = [0] * n_nodes

    def find(self, x):
        if self.par[x] == x:
            return x
        root = self.find(self.par[x])
        self.weights[x] += self.weights[self.par[x]]
        self.par[x] = root
        return root

    def unite(self, x, y, weight=0):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
            self.weights[root_x] = weight - self.weights[x] + self.weights[y]
        else:
            self.par[root_y] = root_x
            self.weights[root_y] = -weight - self.weights[y] + self.weights[x]
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weights[x] - self.weights[y]
import sys
n,m=map(int,input().split())
lrd=[]
tree = WeightedUnionFindTree(n)
for _ in range(m):
    lrd.append(list(map(int,input().split())))
for l,r,d in lrd:
    tree.unite(l-1,r-1,d)
    
for l,r,d in lrd:
    if tree.is_same(l-1,r-1):    
        if tree.diff(l-1,r-1) != d:
            print("No")
            sys.exit()
    else:
        tree.unite(l-1,r-1,d)
else:
    print("Yes")