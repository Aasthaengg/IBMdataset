import sys
#import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ri()
nodes = [set() for _ in range(N+1)]

for _ in range(N-1):
    a, b = rl()
    nodes[a].add(b)
    nodes[b].add(a)

C = rl()
C.sort(reverse=True)
score = sum(C[1:])
deg = [len(x) for x in nodes]
deg_1 = [i for i, x in enumerate(deg) if x == 1]
answer = [0] * (N+1)

while deg_1:
    v = deg_1.pop()
    if not deg_1:
        answer[v] = C.pop()
        break
    w = nodes[v].pop()
    nodes[w].remove(v)
    deg[w] -= 1
    if deg[w] == 1:
        deg_1.append(w)
    answer[v] = C.pop()

print(score)
print(*answer[1:])
