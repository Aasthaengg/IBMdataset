import sys
input = sys.stdin.buffer.readline
import heapq

def main():
	N = int(input())
	edge = [[] for _ in range(N)]
	for _ in range(N-1):
		a,b,d = map(int,input().split())
		edge[a-1].append((b-1,d))
		edge[b-1].append((a-1,d))
	
	Q,K = map(int,input().split())
	dist = [-1]*N
	dist[(K-1)] = 0
	q = [(0,K-1)]
	heapq.heapify(q)
	while q:
		_,now = heapq.heappop(q)
		for fol,d in edge[now]:
			if dist[fol] == -1:
				dist[fol] = dist[now]+d
				heapq.heappush(q,(dist[fol],fol))
	
	for _ in range(Q):
		a,b = map(int,input().split())
		print(dist[a-1]+dist[b-1])
	
if __name__ == "__main__":
	main()
