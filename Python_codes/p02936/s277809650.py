# https://atcoder.jp/contests/abc138/tasks/abc138_d

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


class Graph:
    def __init__(self, n, dictated=False, edge=[]):
        self.n = n
        self.dictated = dictated
        self.conj = [set() for _ in range(self.n)]
        self.visit = set()
        self.second_visit = set()
        for x, y in edge:
            self.add_edge(x,y)

    def add_edge(self,x,y):
        self.conj[x].add(y)
        if self.dictated == False:
            self.conj[y].add(x)

    def dfs(self, info, start=0, goal=None, use_visit=False):
        """
        :param start: スタート地点
        :param goal: ゴール地点
        :param use_visit: 前回の探索結果を保持するかどうか
        :return: ゴール地点までの距離。存在しなければ -1
        """
        if use_visit == False:
            self.visit = set()
            self.second_visit = set()
        self.visit.add(start)

        past_p = None
        next_set = [(start, past_p, 0)]
        next_full_set = [next_set]
        while sum(map(lambda x: x!=[], next_full_set)) != 0:
            next_set = next_full_set.pop()
            p, past_p, t = next_set.pop()
            for q in self.conj[p]:
                if p == past_p:
                    # 逆流した際の処理
                    continue
                if q in self.visit:
                    continue
                if q == goal:
                    # ゴール時の処理
                    # return t+1
                    continue
                # p から q への引継ぎ処理
                info[q] += info[p]
                self.visit.add(q)
                next_set.append((q, p, t + 1))
            if not next_set:
                self.second_visit.add(p)
                # 帰り際の処置（壊した道を元に戻す等)
                # visit.discard(p)
            else:
                next_full_set.append(next_set)
        return info


######################################################################################################

N, Q = map(int, input().split())  # N:頂点数, Q: クエリの数
M = N-1

graph = Graph(N, dictated=False)

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1                                    # デクリメントが不要な場合は消す
    y -= 1
    graph.add_edge(x,y)

info = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    info[p - 1] += x

print(*graph.dfs(info, start=0))
