import sys
from collections import deque

N = int(sys.stdin.readline().strip())

edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

visited = set()
q = {"fennec": deque([0]), "snuke": deque([N-1])}


count = {"fennec": 0, "snuke": 0}
while q["fennec"] or q["snuke"]:
    for user in ("fennec", "snuke"):
        if not q[user]:
            continue
        nq = deque()
        while q[user]:
            point = q[user].popleft()
            for point_next in edges[point]:
                if point_next in visited:
                    continue
                visited.add(point_next)
                count[user] += 1
                nq.append(point_next)
        q[user] = nq

if count["fennec"] > count["snuke"]:
    print("Fennec")
else:
    print("Snuke")