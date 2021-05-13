# https://atcoder.jp/contests/abc075/tasks/abc075_c?lang=ja

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):                                          # 根を見つける関数を定義（同時にxを直接根にくっつける操作も行う）
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])        # 右辺で再帰的に根を探索。根に到達すると一つ目のif判定に引っかかるので、
                                                                # 最終的にself.parents[根]が返ってくる。
                                                                # これを左辺に代入することで、根が親になるように変更する。（根までの距離が長いとO(N)になってしまうので）
            return self.parents[x]

    def union(self, x, y):                                      # 二つの木をくっつける（子を多く持つ方を根とした親子関係）。これは破壊的操作を行う。
        x = self.find(x)                                        # xをxの根に置き換える
        y = self.find(y)                                        # yをyの根に置き換える

        if x == y:                                              # 根が同じなら置き換える必要なし
            return

        if self.parents[x] > self.parents[y]:                   # 子がたくさんある方を x とする（出来るだけ浅い木にするため）
            x, y = y, x

        self.parents[x] += self.parents[y]                      # xの子の数を更新
        self.parents[y] = x                                     # yの親を更新

    def same(self, x, y):                                       # xとyが同じ根の子かを判定
        return self.find(x) == self.find(y)

    def size(self, x):                                          # xの根のparent（= 要素数）を返す
        return -self.parents[self.find(x)]

    def members(self, x):                                       # xが属するグループの要素をリストとして返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):                                            # 全ての根の要素をリストとして返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):                                      # グループの数を返す
        return len(self.roots())

    def all_group_members(self):                                # {根:[根の子のリスト],...}を辞書で返す
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):                                          # print(self) での返し方を定義
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N, M = map(int, input().split())

data = [tuple(map(int, input().split())) for _ in range(M)]
res = 0

for k in range(M):
    tree = UnionFind(N)
    for a, b in data[:k] + data[k+1:]:
        a -= 1
        b -= 1
        tree.union(a,b)
    if tree.group_count() > 1:
       res += 1
print(res)