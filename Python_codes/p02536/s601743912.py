class DisjointSets:
    def __init__(self, n):
        self.nodes = [-1] * n #根にサイズを負の値で格納する。
    def find(self, i):
        if self.nodes[i] < 0: #値が負の場合は根
            return i
        else:
            self.nodes[i] = self.find(self.nodes[i]) #縮約
            return self.nodes[i]
    def unite(self, i, j):
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

n, m = map(int, input().split())
ds = DisjointSets(n)
for _ in range(m):
    a, b = map(lambda x:int(x)-1, input().split())
    ds.unite(a, b)

print(len(set(ds.find(i) for i in range(n))) - 1)