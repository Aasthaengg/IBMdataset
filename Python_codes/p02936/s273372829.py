import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, Q = mapint()
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = mapint()
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
late = [0]*N

for _ in range(Q):
    v, p = mapint()
    late[v-1] += p

ans = [0]*N
checked = [0]*N
from collections import deque
Q = deque([(0, 0)])

while Q:
    v, plus = Q.pop()
    plus += late[v]
    checked[v] = 1
    ans[v] = plus
    for nx in tree[v]:
        if not checked[nx]:
            Q.append((nx, plus))

print(*ans)