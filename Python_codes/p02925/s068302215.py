from collections import defaultdict

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

adj = defaultdict(list)
in_deg = defaultdict(int)
for u, row in enumerate(a, 1):
    for v1, v2 in zip(row, row[1:]):
        uu1, vv1 = min(u, v1), max(u, v1)
        uu2, vv2 = min(u, v2), max(u, v2)
        match1 = uu1 + vv1 * 1000
        match2 = uu2 + vv2 * 1000
        adj[match1].append(match2)
        in_deg[match1]
        in_deg[match2] += 1

now = [key for key, val in in_deg.items() if val == 0]
day = 0
while now:
    day += 1
    nxt = []
    for u in now:
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                nxt.append(v)

    now = nxt

if max(in_deg.values()) > 0:
    day = -1

print(day)
