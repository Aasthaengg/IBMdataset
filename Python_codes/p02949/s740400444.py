import sys
input = sys.stdin.readline


class Graph:
    class Edge:
        def __init__(self, to, cost):
            """
            :param to:  終点ノード
            :param cost: 辺の重み
            """
            self.to, self.cost = to, cost

    def __init__(self, n, directed=False, decrement=True, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.edges2 = []
        self.parent = [-1]*self.n
        self.info = [-1]*self.n
        for x, y, cost in edges:
            self.add_edge(x, y, cost)

    def add_edge(self, x, y, cost):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges2.append((x, y, cost))
        if self.directed == False:
            self.edges2.append((y, x, cost))

    def bellman_ford(self, start, INF=10**18):
        """
        :return: 負の閉路が存在する場合は -1 を返す
        """
        dist = [INF] * self.n
        if self.decrement:
            start -= 1
        dist[start] = 0
        for cnt in range(self.n):
            for x, y, cost in self.edges2:
                if dist[x] != INF and dist[x] + cost < dist[y]:
                    if cnt == self.n - 1:
                        return -1
                    dist[y] = dist[x] + cost
        return dist

    def bellman_ford2(self, start, goal, INF=10**18):
        """
        :return: 負の閉路が存在する場合は -1 を返す
        """
        dist = [INF] * self.n
        if self.decrement:
            start -= 1
            goal -= 1
        dist[start] = 0
        for cnt in range(2*self.n):
            for x, y, cost in self.edges2:
                if dist[x] != INF and dist[x] + cost < dist[y]:
                    dist[y] = dist[x] + cost
                    if cnt >= self.n:
                        dist[y] = -INF
                if cnt == self.n - 1:
                    res = dist[goal]
        if res == dist[goal]:
            return res

    def draw(self):
        """
        :return: グラフを可視化
        """
        import matplotlib.pyplot as plt
        import networkx as nx

        if self.directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        for x, y, cost in self.edges2:
            G.add_edge(x + self.decrement, y + self.decrement, weight=cost)

        edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.axis("off")
        plt.show()



##############################################################################################################

N, M, P = map(int, input().split())
graph = Graph(N, directed=True, decrement=True)
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph.add_edge(x, y, P-cost)

res = graph.bellman_ford2(1,N)
if res is None:
    print(-1)
else:
    print(max(-res,0))