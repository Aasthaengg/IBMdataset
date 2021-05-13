import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


### 木の読み込み tree

# サイズが大きいとdefaultdictが早い(for文を書かなくて済む)
from collections import defaultdict
n = int(input())
ns = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].append(v)
    ns[v].append(u)
    
### BFS 幅優先探索

def bfs(start):
    from collections import deque
    q = deque([start])
    seen = [None] * n
    seen[start] = 0
    while q:
        u = q.pop()
        d = seen[u]
        for v in ns[u]:
            if seen[v] is None:
                seen[v] = d + 1
                q.appendleft(v)
    return seen
d1 = bfs(0)
d2 = bfs(n-1)
v = sum(d1[i]<=d2[i] for i in range(n))
v2 = n-v
if v>v2:
    print("Fennec")
else:
    print("Snuke")