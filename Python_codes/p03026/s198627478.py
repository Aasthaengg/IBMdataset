MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from collections import deque

def main():
    n = int(input())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    
    c = list(map(int,input().split()))
    c.sort(reverse = True)
    
    color = [-1] * n
    s = deque([0])
    i = 0
    while len(s):
        v = s.pop()
        color[v] = c[i]
        for e in G[v]:
            if color[e] != -1:
                continue
            s.append(e)
        i += 1
    
    print(sum(c) - c[0])
    print(*color)
if __name__ =='__main__':
    main()  