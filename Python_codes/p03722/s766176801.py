class BellmanFord:#Union-Find
    def __init__(self, n, init_val = float('inf')):
        self.d = [init_val] * n #根にサイズを負の値で格納する。
        self.init_val = init_val

    def shortest_path(self, s, edges):
        self.d[s] = 0
        for _ in range(n):
            updated = False
            for a, b, w in edges:
                if self.d[a] != self.init_val and self.d[b] > self.d[a] + w:
                    self.d[b] = self.d[a] + w
                    updated = True
            if not updated:
                break
        if updated: #閉路の存在
            for a, b, w in edges:
                if self.d[a] != self.init_val and self.d[b] > self.d[a] + w:
                    self.d[b] = -float('inf')
    
    def get_path_length(self, i):
        return self.d[i]

n, m = map(int, input().split())

edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((a-1, b-1, -w))

bf = BellmanFord(n)
bf.shortest_path(0, edges)
ans = bf.get_path_length(n-1)
print(-ans if ans != -float('inf') else 'inf')