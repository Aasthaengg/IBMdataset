from sys import stdin
def input():
    return stdin.readline().strip()

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
a, b = [], []
for _ in range(m):
    i, j = map(int, input().split())
    edge[i-1].append(j-1)
    edge[j-1].append(i-1)
    a.append(i-1)
    b.append(j-1)

# full search
# DFS
ans = 0
for i in range(m):
    seen = [True] * n
    todo = []
    start = a[i]
    goal = b[i]
    seen[start] = False
    for j in edge[start]:
        if j == goal:
            continue
        else:
            todo.append(j)
            seen[j] = False

    while len(todo) > 0 and seen[goal]:
        j = todo.pop(-1)
        for k in edge[j]:
            if seen[k]:
                todo.append(k)
                seen[k] = False

    if seen[goal]:
        ans += 1

print(ans)