import sys
input = sys.stdin.readline
INF = 10**20
MOD = 10**9 + 7
from itertools import permutations

def main():
    n,m,r = map(int,input().split())
    dest = [int(i) - 1 for i in input().split()]
    dist = [[INF] * n for _ in range(n)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        dist[a][b] = c
        dist[b][a] = c
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])
    
    ans = INF
    for ptr in permutations(range(r)):
        tmp = 0
        for i in range(r - 1):
            tmp += dist[dest[ptr[i]]][dest[ptr[i + 1]]]
        ans = min (ans, tmp)
    
    print(ans)

if __name__=='__main__':
    main()