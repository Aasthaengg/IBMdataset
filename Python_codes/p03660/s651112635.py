from collections import deque
import sys
input = sys.stdin.buffer.readline

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

que = deque()
que.append(1)
root = [-1] * (N+1)
root[1] = 0
while que:
    v = que.popleft()
    for u in adj[v]:
        if root[u] < 0:
            root[u] = v
            que.append(u)

i = N
path = []
while True:
    path.append(i)
    if i == 1:
        break
    i = root[i]
path.reverse()

first = path[(len(path)-1)//2]
second = path[(len(path)-1)//2 + 1]
cnt = 0
que.append(first)
seen = [0] * (N+1)
seen[first] = 1
seen[second] = 1
while que:
    v = que.pop()
    cnt += 1
    for u in adj[v]:
        if seen[u] == 0:
            seen[u] = 1
            que.append(u)

if cnt > N-cnt:
    print('Fennec')
else:
    print('Snuke')

