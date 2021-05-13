class BellmanFord:
    def __init__(self,v,start):
        self.inf = float('inf')
        self.dist = [self.inf]*v
        self.dist[start] = 0
        self.edge = []
        self.v = v
    
    def add(self,f,t,cost):
        self.edge.append((f,t,cost))
    
    def build(self,gorl):
        for _ in range(self.v - 1):
            for f,t,cost in self.edge:
                if self.dist[t] > self.dist[f] + cost:
                    self.dist[t] = self.dist[f] + cost
        self.ans = self.dist[gorl]
        for f,t,cost in self.edge:
            if self.dist[t] > self.dist[f] + cost:
                self.dist[t] = self.dist[f] + cost
        return self.ans if self.ans == self.dist[gorl] else '-inf'

n,m = map(int,input().split())

bf = BellmanFord(n,0)

for i in range(m):
    a,b,c = map(int,input().split())
    bf.add(a - 1,b - 1,- c)

ans = bf.build(n-1)
if ans == '-inf':
    print('inf')
else:
    print(- ans)
