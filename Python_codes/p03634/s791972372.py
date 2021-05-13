def ij2str(i, j):
    return str(i) + '+' + str(j)

n = int(input())
tree = [[] for _ in range(n)]
dis = [0 for _ in range(n)]
c_list = {}
visited = set()
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    c_list[ij2str(a-1, b-1)] = c
    c_list[ij2str(b-1, a-1)] = c

from collections import deque

q, k = map(int, input().split())
visited.add(k-1)
next = deque()
next.append(k-1)

while len(next):
    i = next.popleft()
    for j in tree[i]:
        if not j in visited:
            dis[j] = dis[i] + c_list[ij2str(i, j)]
            next.append(j)
            visited.add(j)

for i in range(q):
    x, y = map(int, input().split())
    print(dis[x-1] + dis[y-1])
