import sys
INF = 10**10
MOD = 10**9 + 7
sys.setrecursionlimit(100000000)
from functools import lru_cache
from itertools import permutations

def main():
    n,m = map(int,input().split())
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    edge = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        dist[a][b] = c
        dist[b][a] = c
        edge.append((a,b,c))
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    
    cnt = 0
    for e in edge:
        a,b,c = e
        flag = True
        for i in range(n):
            for j in range(n):
                if dist[i][a] + c + dist[b][j] == dist[i][j]:
                    flag = False
                    break
            if flag == False:
                break
        
        if flag:
            cnt += 1
    
    print(cnt)

if __name__=='__main__':
    main() 