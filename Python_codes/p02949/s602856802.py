inf = float('inf')
# ベルマンフォード法 計算量(VE)
# [引数]: 隣接リスト, 始点, 終点
class Bellmanford:
    def __init__(self, to : list, start : int, goal : int):
        self.N = len(to)
        self.to = [s[:] for s in to]
        self.start = start
        self.goal = goal
        self.dist = [inf] * self.N
        self.dist[start] = 0
    
    # self.distを更新
    def update(self) -> None:
        for _ in range(self.N - 1):
            for v, s in enumerate(self.to):
                if not s: continue
                for nv, w in s:
                    if self.dist[nv] > self.dist[v] + w:
                        self.dist[nv] = self.dist[v] + w
    
    # グラフの負閉路検出
    def detection(self) -> bool:
        exists_negative_cycle = False
        for v, s in enumerate(self.to):
            if not s: continue
            for nv, w in s:
                if self.dist[nv] > self.dist[v] + w:
                    self.dist[nv] = self.dist[v] + w
                    exists_negative_cycle = True
        return exists_negative_cycle
    
    # スタートからゴールまでのパスの負閉路検出
    def detection_stog(self) -> bool:
        exists_negative_cycle_stog = False
        is_updated = [False] * self.N
        for _ in range(self.N):
            for v, s in enumerate(self.to):
                if not s: continue
                for nv, w in s:
                    if self.dist[nv] > self.dist[v] + w:
                        self.dist[nv] = self.dist[v] + w
                        is_updated[nv] = True
                    if is_updated[v] is True:
                        is_updated[nv] = True
        exists_negative_cycle_stog = is_updated[self.goal]
        return exists_negative_cycle_stog

N, M, P = map(int,input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int,input().split())
    A -= 1; B -= 1
    C -= P
    to[A].append((B, -C))

BF = Bellmanford(to, 0, N-1)
BF.update()

if BF.detection_stog():
    ans = -1
else:
    ans = max(-BF.dist[N-1], 0)

print(ans)