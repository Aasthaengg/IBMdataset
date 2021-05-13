import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class UF_tree:
    def __init__(self, n):
        self.root = [-1] * (n + 1)  # -1ならそのノードが根,で絶対値が木の要素数
        self.rank = [0] * (n + 1)

    def find(self, x):  # xの根となる要素番号を返す
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def getNodeLen(self, x):
        return -self.root[self.find(x)]


if __name__ == "__main__":
    N, M = map(int, input().split())
    AB = tuple(tuple(map(int, input().split())) for _ in range(M))
    score = N * (N - 1) // 2

    ans = [score]
    uf = UF_tree(N)
    for a, b in AB[::-1]:
        if uf.isSame(a, b):
            ans.append(score)
            continue
        x = uf.getNodeLen(a)
        y = uf.getNodeLen(b)
        uf.unite(a, b)
        score -= x * y
        ans.append(score)
    ans.reverse()
    print(*ans[1:], sep="\n")