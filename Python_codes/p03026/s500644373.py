from collections import deque
import sys
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _i in range(n)]
for _i in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

c = deque(sorted(list(map(int, input().split())), reverse=True))
visit = [-1 for _i in range(n)]
visit[0] = c.popleft()

def solve(p):
    r = 0
    for i in tree[p]:
        if visit[i] < 0:
            visit[i] = c.popleft()
            r += visit[i]
            r += solve(i)
    return r
x = solve(0)
print(x)
print(*visit)