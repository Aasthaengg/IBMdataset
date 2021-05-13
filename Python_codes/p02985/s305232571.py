def getlist():
	return list(map(int, input().split()))

from collections import defaultdict
import queue

const = 10 ** 9 + 7
INF = float("inf")

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def get_nodes(self):
        return self.graph.keys()

class BFS(object):
	def __init__(self, graph, s, N, K):
		self.ans = 1
		self.g = graph.graph
		self.Q = queue.Queue()
		self.W = [len(self.g[i]) for i in range(N)]
		self.visit = ["No"] * (N + 1) #見たか判定
		self.visit[s] = "Yes"
		#startの処理
		for i in self.g[s]:
			self.Q.put(i)
		if self.W[0] + 1 > K:
			self.ans = 0
		else:
			for i in range(self.W[0] + 1):
				self.ans = (self.ans * (K - i)) % const

		#start以降の処理
		while not self.Q.empty():
			v = self.Q.get()
			for i in self.g[v]:
				if self.visit[i] == "No":
					if self.W[i] + 1 > K:
						self.ans = 0
					else:
						for j in range(self.W[i] - 1):
							self.ans = (self.ans * (K - 2 - j)) % const
					self.Q.put(i)
					self.visit[i] = "Yes"

	def answer(self):
		return self.ans

#受け取り、初期化
N, K = getlist()
G = Graph()
for i in range(N - 1):
	a, b = getlist()
	G.add_edge(a - 1, b - 1)
	G.add_edge(b - 1, a - 1)
s = 0

#幅優先探索
W = BFS(G, 0, N, K)
print(W.answer())
