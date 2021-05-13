MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

MAXN = 10000
G = [[] for _ in range(MAXN)]
color = [-1] * MAXN

def dfs(i,idx,c):
    color[i] = c[idx]
    for e in G[i]:
        if color[e] != -1:
            continue
        idx = dfs(e,idx + 1,c)
    return idx

def main():
    n = int(input())
    for _ in range(n - 1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    
    c = list(map(int,input().split()))
    c.sort(reverse = True)

    dfs(0,0,c)
    ans = sum(c) - c[0]
    print(ans)
    print(*color[:n])

if __name__ =='__main__':
    main()  