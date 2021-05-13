import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
uvw = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    uvw[u].append([v, w])
    uvw[v].append([u, w])
color = [-1 for _ in range(n)]
color[0] = 0
def dfs(before_pos, pos, w):
    color[pos] = w
    for next_pos, next_w in uvw[pos]:
        if next_pos == before_pos:
            continue
        dfs(pos, next_pos, (w + next_w) % 2)
    
dfs(-1, 0, 0)
for c in color:
    print(c)