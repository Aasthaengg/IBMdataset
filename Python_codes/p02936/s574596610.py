from collections import defaultdict

N, Q = map(int, input().split())
edges = defaultdict(set)
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)
PX = []
for _ in range(Q):
    PX.append(list(map(int, input().split())))

direct_score = defaultdict(int)
final_score = {}

for px in PX:
    direct_score[px[0]] += px[1]

stack = [(1, 0)]

while stack:
    node, score = stack.pop()
    if node in final_score:
        continue
    score += direct_score[node]
    final_score[node] = score
    for child in edges[node]:
        stack.append((child, score))

print(' '.join([str(final_score[i]) for i in range(1, N+1)]))