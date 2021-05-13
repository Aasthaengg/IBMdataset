import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w = map(int, input().split())
rows,cols = h,w

OK = "."
NG = "#"

from collections import defaultdict

ns = defaultdict(set)
ss = [None] * rows
for i in range(rows):
    s = input()
    ss[i] = s
    for j,c in enumerate(s):
        u = i*cols+j
        if i>0:
            if c==OK and ss[i-1][j]==OK:
                v = u - cols
                ns[u].add(v)
                ns[v].add(u)
        if j>0:
            if c==OK and s[j-1]==OK:
                v = u - 1
                ns[u].add(v)
                ns[v].add(u)
                    
n = rows * cols

def bfs(start):
    from queue import deque
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
ans = -1
for i in range(rows):
    for j in range(cols):
        if ss[i][j] == "#":
            continue
        u = i*cols+j
        dist = bfs(u)
        ans = max(ans, max(num for num in dist if num is not None))
print(ans)