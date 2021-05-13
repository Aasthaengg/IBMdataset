from collections import deque


class TPSort:
    """
    トポロジカルソート
    # https://csacademy.com/lesson/topological_sorting/

    # 入次数0のノードから確定し, そのノードから伸びるエッジを削除. を繰り返すことによって DAGのソートをする
    """

    def __init__(self, N):
        self.N = N
        self.indegree = [0] * N  # 入次数
        self.length = [0] * N
        self.edges = [[] for _ in range(N)]

    def add_edge(self, a, b):
        self.edges[a].append(b)
        self.indegree[b] += 1

    def sort(self):
        que = deque([i for i in range(self.N) if self.indegree[i] == 0])

        res = []
        while que:
            n = que.popleft()
            res.append(n)
            for next_n in self.edges[n]:
                self.length[next_n] = max(self.length[next_n], self.length[n] + 1)
                self.indegree[next_n] = self.indegree[next_n] - 1  # 枝刈り
                if self.indegree[next_n] == 0:  # 入次数0なら queue に追加
                    que.append(next_n)
        return res


if __name__ == '__main__':
    n, m = [int(_) for _ in input().split()]
    tp = TPSort(n + 1)

    for i in range(m):
        tp.add_edge(*[int(_) for _ in input().split()])

    tp.sort()
    print(max(tp.length))
