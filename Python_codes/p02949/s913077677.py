import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces
 
n, m, p = na()
 
def bf(es, n, start):
    d = [999999999999] * n
    d[start] = 0
 
    for r in range(n-1):
        updated = False
        for e in es:
            if d[e[0]] == 999999999999:
                continue
            if d[e[0]] + e[2] < d[e[1]]:
                d[e[1]] = d[e[0]] + e[2]
                updated = True
        if not updated:
            break
 
    for e in es:
        if d[e[0]] < 999999999999 and d[e[0]] + e[2] < d[e[1]]:
            return None
 
    return d
 
es = []
for i in range(m):
    a, b, c = na()
    es.append((a-1, b-1, -(c-p)))
 
import collections
q = collections.deque()
q.append(n-1)
 
valid = [False] * n
valid[n-1] = True
while len(q) > 0:
    cur = q.popleft()
    for e in es:
        if e[1] == cur and not valid[e[0]]:
            valid[e[0]] = True
            q.append(e[0])
 
nes = []
for e in es:
    if valid[e[0]] and valid[e[1]]:
        nes.append(e)
es = nes
 
d = bf(es, n, 0)
if not d:
    print(-1)
else:
    print(max(0, -d[n-1]))