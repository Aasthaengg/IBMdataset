import sys 
MOD = 10 ** 9 + 7
INF = 10**5
from collections import deque

def main():
    n = int(input())
    dist = []
    edge = []
    ans = 0
    for i in range(n):
        a = list(map(int,input().split()))
        dist.append(a)
        for j in range(n):
            if i < j:
                edge.append((a[j],i,j))
                ans += a[j]
    
    for k in range(n - 1):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j] ,dist[i][k] + dist[k][j])
    
    edge.sort(reverse = True,key = lambda x:x[0])
    for c,a,b in edge:
        if dist[a][b] < c:
            ans = -1
            break
        for i in range(n):
            if i != a and i != b:
                if c == dist[a][i] + dist[i][b]:
                    ans -= c
                    break
    print(ans)   

if __name__=='__main__':
    main()