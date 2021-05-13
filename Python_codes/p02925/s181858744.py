n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def match2int(x, y):
    x, y = min(x, y), max(x, y)
    return (2 * n - 1 - x) * x // 2 + y - x - 1


match_sm = n * (n - 1) // 2

adj = [[] for _ in range(match_sm)]
in_deg = [0] * match_sm
for i, li in enumerate(a):
    for j, k in zip(li, li[1:]):
        j -= 1
        k -= 1
        match1 = match2int(i, j)
        match2 = match2int(i, k)
        adj[match1].append(match2)
        in_deg[match2] += 1

cnd = [i for i, e in enumerate(in_deg) if e == 0]
day = 0
while cnd:
    nxt_cnd = []
    for u in cnd:
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                nxt_cnd.append(v)

    cnd = nxt_cnd
    day += 1

if in_deg.count(0) != match_sm:
    day = -1

print(day)
