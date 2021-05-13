import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    
    def BellmanFord(edges,V,source):
        INF = float("inf")
        dist = [INF for _ in range(N)]
        dist[source] = 0
        
        for i in range(V):
            for now,fol,d in edges:
                if dist[now] != INF and dist[fol] > dist[now]+d:
                    dist[fol] = dist[now]+d
                    if i == V-1 and fol == N-1:
                        return "inf"
        return -1*dist[-1]
        
    edge = []
    for _ in range(M):
        a,b,c = map(int,input().split())
        edge.append((a-1,b-1,-c))
    
    print(BellmanFord(edge,N,0))

if __name__ == "__main__":
    main()
