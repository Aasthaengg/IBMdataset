import sys
input = sys.stdin.readline
import marshal


class Graph:
    def __init__(self, n, directed=False, decrement=True, destroy=False, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.destroy = destroy
        self.edges = [set() for _ in range(self.n)]
        self.parent = [-1]*self.n
        self.info = [-1]*self.n
        for x, y in edges:
            self.add_edge(x,y)

    def add_edge(self, x, y):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].add(y)
        if self.directed == False:
            self.edges[y].add(x)

    def dfs2(self, info, start=1, goal=-1, time=0, save=False):
        """
        :param info: 各頂点の付加情報 = [v1,v2,v3,...,vN]
        :param start: スタート地点
        :param goal: ゴール地点
        :param save: True = 前回の探索結果を保持する
        :return: 伝搬後のinfo
        """

        if self.decrement:
            start -= 1
            goal -= 1
        if not save:
            self.parent = [-1] * self.n
        if self.destroy:
            edge2 = self.edges
        else:
            edge2 = marshal.loads(marshal.dumps(self.edges))

        p, t = start, time
        self.parent[p] = -2
        while True:
            if edge2[p]:
                q = edge2[p].pop()
                if q == self.parent[p] and not self.directed:
                    """ 逆流した時の処理 """
                    """"""""""""""""""""
                    continue
                if self.parent[q] != -1:
                    """ サイクルで同一点を訪れた時の処理 """
                    """"""""""""""""""""
                    continue
                if q == goal:
                    """ ゴール時の処理"""
                    # return t + 1
                    """"""""""""""""""""
                    continue
                """ p から q への引継ぎ"""
                info[q] += info[p]
                """"""""""""""""""""
                self.parent[q] = p
                p, t = q, t + 1
            else:
                """ p から進める点がもう無い時の点 p における処理 """
                """"""""""""""""""""
                if p == start and t == time:
                    break
                p, t = self.parent[p], t-1
                """ 点 p から親ノードに戻ってきた時の親ノードにおける処理 """

                """"""""""""""""""""
        return info

##################################################################################################

N, Q = map(int, input().split())
M = N-1
graph = Graph(N, directed=False, decrement=True, destroy=False)
for _ in range(M):
    x, y = map(int, input().split())
    graph.add_edge(x, y)
info = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    info[p-1] += x
res = graph.dfs2(info, start=1)
print(*res)