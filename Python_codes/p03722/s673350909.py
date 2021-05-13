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
        self.exists_negative_cycle = False
        self.exists_negative_cycle_stog = False
        self.is_updated = [False] * self.N
    
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
        for v, s in enumerate(self.to):
            if not s: continue
            for nv, w in s:
                if self.dist[nv] > self.dist[v] + w:
                    self.dist[nv] = self.dist[v] + w
                    self.exists_negative_cycle = True
        return self.exists_negative_cycle
    
    # スタートからゴールまでのパスの負閉路検出
    def detection_stog(self) -> bool:
        for _ in range(self.N):
            for v, s in enumerate(self.to):
                if not s: continue
                for nv, w in s:
                    if self.dist[nv] > self.dist[v] + w:
                        self.dist[nv] = self.dist[v] + w
                        self.is_updated[nv] = True
                    if self.is_updated[v] is True:
                        self.is_updated[nv] = True
        self.exists_negative_cycle_stog = self.is_updated[self.goal]
        return self.exists_negative_cycle_stog

N, M = map(int,input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int,input().split())
    a -= 1; b -= 1
    to[a].append((b, -c))

BF = Bellmanford(to, 0, N-1)
BF.update()

if BF.detection_stog():
    ans = "inf"
else:
    ans = -BF.dist[N-1]

print(ans)