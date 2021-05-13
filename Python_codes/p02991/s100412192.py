from heapq import heappush, heappop
inf = float('inf')
mod = 10**9 + 7

# ダイクストラ法 計算量O(ElogV)
# [引数]: 隣接リスト, 始点
class Dijkstra:
    def __init__(self, to:list, start:int):
        self.N = len(to)
        self.to = [s[:] for s in to]
        self.start = start
        self.dist = [inf] * self.N
        self.dist[start] = 0
        # cnt : 最短経路の数
        self.cnt = [0] * self.N
        self.cnt[start] = 1
        self.pq = [(self.dist[start], start)]

    # distを更新
    def update(self) -> None:
        while self.pq:
            _, v = heappop(self.pq)
            for nv, w in self.to[v]:
                if self.dist[nv] > self.dist[v] + w:
                    self.dist[nv] = self.dist[v] + w
                    heappush(self.pq, (self.dist[nv], nv))
                if self.dist[nv] == self.dist[v] + w:
                    self.cnt[nv] += self.cnt[v]
                    self.cnt[nv] %= mod

N, M = map(int,input().split())
to = [[] for _ in range(3*N)]
for _ in range(M):
    u, v = map(int,input().split())
    u -= 1; v -= 1
    for i in range(3):
        nu = 3*u + i
        nv = 3*v + (i + 1) % 3
        to[nu].append((nv, 1))
S, T = map(int,input().split())
S -= 1; T -= 1

DI = Dijkstra(to, 3*S)
DI.update()

ans = DI.dist[3*T]
if ans == inf:
    ans = -1
else:
    ans //= 3
print(ans)