import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

class UnionFind():
    """
    https://note.nkmk.me/python-union-find/
    DFSの上位互換と考えて良い
    ２要素x, yがpath-connectedかどうかをlogオーダーで判定する（螺旋本の14.1節参照）
    さらに連結成分の要素数がO(1)で取得可能なように改造してある
    """
    def __init__(self, n):
        """
        要素数をnとして、各ノードを0,1,...,(n-1)の番号で管理する
        parentsは各ノードの属する木の根を表す
        ただし根ノードのparentには(その木のノード数)*(-1)を格納する
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        xの属する木の根を返す
        このとき同時に経路圧縮して、探索途中のノードを全て根に繋ぎ直す
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        x, yのそれぞれ属する木Tx, Tyの根同士を繋ぐ
        このとき木の要素数が小さい方を大きい方に繋ぐ（rankではなくsizeを用いる）
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        xの属する木の要素数を返す
        根の親を要素数の(-1)倍で定めておいたおかげでO(1)で取得可能
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        xとyがpath-connectedかを判定する
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        xの属する木の要素を列挙する
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        連結成分の代表元のリストを返す
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        連結成分の個数を返す
        """
        return len(self.roots())

    def all_group_members(self):
         """
         連結成分およびそれぞれの代表元をまとめた辞書を返す
         代表元がキーになってる
         """
         return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        """
        連結成分およびその代表元を出力
        """
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    N = int(input())
    repn = [[] for _ in range(N)]
    edge = []
    for _ in range(N - 1):
        a, b = map(int, input().split())
        repn[a - 1].append(b - 1)
        repn[b - 1].append(a - 1)
        if a > b: a, b = b, a
        edge.append((a - 1, b - 1))

    """
    まさかの問題を読み間違えていた。。。
    （プレイヤーがマスの上を１マスずつ動くと思っていた）

    「最適に行動した時」＝「どちらかに必勝法が存在する」と言い換える。
    あとはその戦略を見出せば勝ち。見抜けなければ相手の全行動パターンに勝つ手の存在を示す。
    同じ色が隣接していればどのマスでも塗れるなら、最初に一気に２人が距離を詰めた方がいいに決まってる。
    """

    # 頂点０からのdepthを求める
    depth_from_0 = [-1] * N
    parent = [-1] * N
    depth_from_0[0] = 0

    def dfs(u):
        for v in repn[u]:
            if depth_from_0[v] != -1: continue
            depth_from_0[v] = depth_from_0[u] + 1
            parent[v] = u
            dfs(v)

    dfs(0)

    # ２人を結ぶパスの同定
    path = [N - 1]
    while path[-1] != 0: path.append(parent[path[-1]])
    l = len(path)

    # ２人が互いに塗るマスの数を計算
    tree = UnionFind(N)
    a0, b0 = path[l // 2 - 1], path[l // 2]
    if a0 > b0: a0, b0 = b0, a0
    for a, b in edge:
        if a != a0 or b != b0: tree.union(a, b)
    Fennec = tree.size(0)
    Snuke = tree.size(N - 1)
    if Fennec > Snuke:
        print("Fennec")
    else:
        print("Snuke")



if __name__ == "__main__":
    main()
