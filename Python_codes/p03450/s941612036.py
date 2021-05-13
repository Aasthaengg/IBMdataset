from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
E = [[] for i in range(n)]
for i in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    E[l].append((r, d))
    E[r].append((l, -d))

pos = {}

def bfs(cur, pre, p):
    stack = deque([(cur, pre, p)])
    while stack:
        cur, pre, p = stack.popleft()
        if cur in pos:
            if p != pos[cur]:
                print('No')
                sys.exit()
        else:
            pos[cur] = p

            for e, d in E[cur]:
                if e != pre:
                    stack.append([e, cur, p + d])

for i in range(n):
    if i in pos:
        continue
    bfs(i, -1, 0)

print('Yes')