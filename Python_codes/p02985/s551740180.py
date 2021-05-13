from sys import stdin
from collections import deque

N, K = [int(x) for x in stdin.readline().rstrip().split()]
AB = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N - 1)]

tree = [[] for _ in range(N)]
inf = 10 ** 9 + 7

for i in range(N - 1):
    tree[AB[i][0] - 1].append(AB[i][1] - 1)
    tree[AB[i][1] - 1].append(AB[i][0] - 1)

ans = 1
q = deque([0])
visited = [False] * N

while len(q) > 0:
    c = q.popleft()
    visited[c] = True
    if c == 0:
        m = K - 1
        ans *= K
        ans %= inf
    else:
        m = K - 2
    for i in range(len(tree[c])):
        if not visited[tree[c][i]]:
            ans *= m
            ans %= inf
            m -= 1
            q.append(tree[c][i])

print(ans)