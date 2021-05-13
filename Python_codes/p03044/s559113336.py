from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

class edge:
    def __init__(self, to, cost):
        self.to, self.cost = to, cost

def main():
    N = int(input())
    g = defaultdict(list)
    for i in range(N-1):
        u, v, w = (int(_) for _ in input().split())
        g[u].append(edge(v, w))
        g[v].append(edge(u, w))

    color = [0] * (N+1)

    def dfs(ver):
        for e in g[ver]:
            if color[e.to] == 0 and e.cost%2 == 0:
                color[e.to] = color[ver]
                dfs(e.to)
            elif color[e.to] == 0 and e.cost%2 == 1:
                color[e.to] = (-1) * color[ver]
                dfs(e.to)
    color[1] = 1
    dfs(1)
    for i in range(1, N+1):
        if color[i] == -1: color[i] = 0
    print(*color[1:], sep='\n')
    return

if __name__ == '__main__':
    main()
