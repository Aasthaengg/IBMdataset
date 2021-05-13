#整数値入力 1文字の入力
def input_one_number():
    return int(input())

#整数値龍力　複数の入力
def input_multiple_number():
    return map(int, input().split())

#整数値龍力　複数の入力(配列)
def input_multiple_number_as_list():
    return list(map(int, input().split()))


n,m = input_multiple_number()

#UnionFind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    #要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    #要素xが属するグループのサイズ（要素数）を返す
    def getGroupSize(self, x):
        return -self.parents[self.find(x)]

    #要素x, yが同じグループに属するかどうかを返す
    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    #要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    #すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    #グループの数を返す
    def getNumGroup(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

re = UnionFind(n)

for _ in range(m):
	a,b = input_multiple_number()
	re.union(a-1,b-1)

mmax = 0
for nood in re.roots():
	g = re.getGroupSize(nood)
	if mmax < g:
		mmax = g
print(mmax)