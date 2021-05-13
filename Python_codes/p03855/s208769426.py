class UnionFindTree:
    def __init__(self, n):
        self.nodes = [-1] * n #根にサイズを負の値で格納する。
    def find(self, i):
        if self.nodes[i] < 0: #値が負の場合は根
            return i
        else:
            self.nodes[i] = self.find(self.nodes[i]) #縮約
            return self.nodes[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        if self.nodes[i] > self.nodes[j]: #サイズ比較してiの方がサイズが大きいようにする
            i, j = j, i
        self.nodes[i] += self.nodes[j] #大きい方に小さい方を統合しサイズを登録する。
        self.nodes[j] = i # jの親はi
    
    def size(self, i): # 所属する集合の大きさを返す
        i = self.find(i)
        return -self.nodes[i]


n, k, l = map(int, input().split())
roads = UnionFindTree(n)
railways = UnionFindTree(n)
ans = []
for _ in range(k):
    a, b = map(lambda x : int(x) - 1, input().split())
    roads.union(a, b)
    
for _ in range(l):
    a, b = map(lambda x : int(x) - 1, input().split())
    railways.union(a, b)

counter = dict()
for i in range(n):
    p = (roads.find(i), railways.find(i))
    if not p in counter:
        counter[p] = 1
    else:
        counter[p] += 1

ans = [counter[(roads.find(i), railways.find(i))] for i in range(n)]
print(" ".join(map(str, ans)))