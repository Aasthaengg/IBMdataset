#####################################################################################################
##### Low Link (橋、関節点)
#####################################################################################################

"""

計算量
O(V+E)

参考
https://algo-logic.info/bridge-lowlink/


"""



import sys
input = sys.stdin.readline
import marshal


class Graph:
    def __init__(self, n, dictated=False, decrement=True, destroy=False, edges=[]):
        self.n = n
        self.dictated = dictated
        self.decrement = decrement
        self.destroy = destroy
        self.edges = [set() for _ in range(self.n)]
        self.parent = [-1]*self.n
        for x, y in edges:
            self.add_edge(x,y)

    def add_edge(self, x, y):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].add(y)
        if self.dictated == False:
            self.edges[y].add(x)

    def add_adjacent_list(self, i, adjacent_list):
        if self.decrement:
            self.edges[i] = set(map(lambda x: x - 1, adjacent_list))
        else:
            self.edges[i] = set(adjacent_list)

    def bridge_detector(self, articular_list=False):
        """
        :param p: スタート地点
        :param save: True = 前回の探索結果を保持する
        :param articular_list: True = 関節点のリストを返す
        :return: 各点までの距離と何番目に発見したかを返す
        """

        if self.destroy:
            edge2 = self.edges
        else:
            edge2 = marshal.loads(marshal.dumps(self.edges))

        start, time = 0, 0
        p, t = start, time
        self.parent[p] = -2
        ord = [-1]*self.n       # ord = DFS で頂点 q を何番目に探索したか
        ord[p] = t
        low = [-1]*self.n       # low = q からの 0 回以上木辺を使って前進し、後退辺を1回以下使って後退する事で到達できる頂点 p について、ord[p] の最小値
        low[p] = 0
        articular = []          # 関節点の集合
        bridge = []             # 橋の集合

        if len(edge2[p]) >= 2:
            """ 根に子が二つ異常存在する場合は、根も関節点 """
            articular.append(p)

        while True:
            if edge2[p]:
                q = edge2[p].pop()
                if q == self.parent[p] and not self.dictated:
                    """ 逆流した時の処理 """
                    """"""""""""""""""""
                    continue
                if self.parent[q] != -1:
                    """ サイクルで同一点を訪れた時の処理 """
                    if ord[q] < low[p]:
                        low[p] = ord[q]
                    """"""""""""""""""""
                    continue
                """ p から q への引継ぎ"""
                """"""""""""""""""""
                ord[q] = low[q] = t + 1
                self.parent[q] = p
                p, t = q, t + 1
            else:
                if p == start and t == time:
                    break
                """ p から進める点がもう無い時の点 p における処理 """
                parent_p = self.parent[p]
                if low[p] < low[parent_p]:
                    low[parent_p] = low[p]
                """ この時点でlow[p]が確定するので、ord[parent[p]] ≤ low[p] を判定しておく"""
                if ord[parent_p] <= low[p]:
                    if ord[parent_p]:
                        articular.append(parent_p + self.decrement)
                    if ord[parent_p] < low[p]:
                        bridge.append((parent_p + self.decrement, p + self.decrement))
                """"""""""""""""""""
                p, t = self.parent[p], t - 1
                """ 点 p から親ノードに戻ってきた時の親ノードにおける処理 """
                """"""""""""""""""""
        if articular_list == False:
            return bridge
        else:
            return articular

    def draw(self):
        """
        :return: グラフを可視化
        """
        import matplotlib.pyplot as plt
        import networkx as nx

        if self.dictated:
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        for x in range(self.n):
            for y in self.edges[x]:
                G.add_edge(x + self.decrement, y + self.decrement)

        nx.draw_networkx(G)
        plt.show()


def inc(A):
    return list(map(lambda x: x+1, A))


def dec(A):
    return list(map(lambda x: x-1, A))

###############################################################################################

N, M = map(int, input().split())
graph = Graph(N, dictated=False, decrement=True, destroy=False)
for _ in range(M):
    x, y = map(int, input().split())
    graph.add_edge(x, y)



print(len(graph.bridge_detector(articular_list=False)))

# graph.draw()

"""
9 10
7 8
8 9
3 6
9 2
1 2
2 3
3 4
4 5
5 6
6 7

"""