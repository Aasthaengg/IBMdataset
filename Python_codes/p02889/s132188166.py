import sys
input = sys.stdin.readline
import numpy as np
from scipy.sparse.csgraph import floyd_warshall

def main():
    N,M,L = map(int,input().split())
    edge = np.zeros((N,N))
    for _ in range(M):
        a,b,c = map(int,input().split())
        edge[a-1][b-1] = edge[b-1][a-1] = c
        
    length = floyd_warshall(edge,directed=False)
    ref = np.where(length<=L,1,0)
    ans = floyd_warshall(ref,directed=False)
    Q = int(input())
    for _ in range(Q):
        s,t = map(int,input().split())
        if ans[s-1][t-1] == float("inf"):
            print(-1)
        else:
            print(int(ans[s-1][t-1])-1)

if __name__ == "__main__":
    main()
