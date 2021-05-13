from collections import defaultdict, deque

N = int(input())
edges = {}
scores = defaultdict(lambda: -1)

for _ in range(N):
    l = list(map(int, input().split()))
    node = l[0]
    degree = l[1]
    edges[node] = l[2:]

q = deque()
q.append((1, 0))

while q:
    node, score = q.popleft()
    if scores[node] != -1:
        continue
    scores[node] = score
    for child in edges[node]:
        q.append((child, score+1))

for node in range(1, N+1):
    print('%d %d' % (node, scores[node]))


