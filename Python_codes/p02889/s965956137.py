from scipy.sparse import csr_matrix #pypyだとエラーになるので、pythonを使うこと
from scipy.sparse.csgraph import shortest_path, floyd_warshall
import numpy as np

import sys
def input():
	return sys.stdin.readline().strip()

N, M, L = list(map(int, input().split()))

A = np.zeros(M)
B = np.zeros(M)
C = np.zeros(M)
for i in range(M):
	Ai, Bi, Ci = list(map(int, input().split()))
	A[i] = Ai - 1
	B[i] = Bi - 1
	C[i] = Ci

graph = csr_matrix((C, (A, B)), shape=(N, N))
#print(graph)
dist = floyd_warshall(graph, directed=False)
graph2 = np.full((N, N), np.inf)
for i in range(N):
	for j in range(N):
		if dist[i, j] <= L:
			graph2[i, j] = 1
graph2 = csr_matrix(graph2)
num = shortest_path(graph2, directed=False)


Q = int(input())
for q in range(Q):
	s, t = list(map(int, input().split()))
	if num[s - 1][t - 1] < 10000000:
		print(int(num[s - 1][t - 1] - 1))
	else:
		print(-1)