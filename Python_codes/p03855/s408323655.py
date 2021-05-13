from collections import deque

n, k, l = map(int, input().split())

graphs = [[[] for _ in range(n)], [[] for _ in range(n)]]
cands = [set(), set()]
for _ in range(k):
    x, y = map(int, input().split())
    graphs[0][x - 1].append(y - 1)
    graphs[0][y - 1].append(x - 1)
    cands[0].add(x - 1)
for _ in range(l):
    x, y = map(int, input().split())
    graphs[1][x - 1].append(y - 1)
    graphs[1][y - 1].append(x - 1)
    cands[1].add(x - 1)

groups = [[], []]
groups_inv = [[-1] * n, [-1] * n]
def dfs(start, case, num):
    q = deque()
    q.append(start)
    used = {start}
    groups[case].append(used)
    groups_inv[case][start] = num
    while q:
        node = q.popleft()
        for to in graphs[case][node]:
            if to in used:
                continue
            q.append(to)
            used.add(to)
            groups_inv[case][to] = num

for i in range(2):
    count = 0
    for node in cands[i]:
        if groups_inv[i][node] == -1:
            dfs(node, i, count)
            count += 1

ret = [-1] * n
for i in range(n):
    if groups_inv[0][i] == -1 or groups_inv[1][i] == -1:
        ret[i] = 1
    elif ret[i] == -1:
        cities = groups[0][groups_inv[0][i]] & groups[1][groups_inv[1][i]]
        for city in cities:
            ret[city] = len(cities)
print(*ret)
