# G[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
# クラスにしてしまったけど、これ遅いのでクラスじゃ無い方が良い
class Warshall_Floyd:
    def __init__(self, V):
        self.V = V
        self.G = [[float('inf')] * self.V for i in range(self.V)]

    def add_edge(self, fr, to, cost):
        self.G[fr][to] = cost

    def add_multi_edge(self, v1, v2, cost):
        self.G[v1][v2] = cost
        self.G[v2][v1] = cost

    def solve(self):
        for i in range(self.V):
            self.G[i][i] = 0
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.G[i][k] != float("inf") and self.G[k][j] != float('inf'):
                        self.G[i][j] = min(self.G[i][j], self.G[i][k] + self.G[k][j])

    def if_negative(self):
        for i in range(self.V):
            if self.G[i][i] < 0:
                return True
        return False

    def dist(self, fr, to):
        return self.G[fr][to]


G = Warshall_Floyd(10)

H, W = map(int, input().split())
for i in range(10):
    for j, c in enumerate(input().split()):
        G.add_edge(i, j, int(c))
G.solve()


ans = 0
for i in range(H):
    for j, a in enumerate(input().split()):
        if a != "-1":
            ans += G.dist(int(a), 1)

print(ans)