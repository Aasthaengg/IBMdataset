import sys

def tree_path():
    def walk(i,c):
        if d[i] == -1:
            d[i] = c
            for node, dist in path[i]:
                walk(node, c+dist)
    sys.setrecursionlimit(100007)
    n = int(input())
    path = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u , v , w = map(int,input().split())
        path[u].append([v,w])
        path[v].append([u,w])
    
    d = [-1] * (n+1)
    walk(1,0)
    for item in d[1:]:
        print(item % 2)
tree_path()