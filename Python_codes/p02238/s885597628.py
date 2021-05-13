def dfs(v, u=0):
    global n, t, d, f, reached
    if len(reached) == n:
        return

    d[u] = t
    t += 1

    reached.add(u + 1)
    for ui in range(v[u][1]):
        next = v[u][2 + ui]
        if next in reached:
            continue
        dfs(v, next - 1)

    f[u] = t
    t += 1


n = int(input())
v = []
for _ in range(n):
    v.append(list(map(int, input().split())))

t = 1
d = [0] * n
f = [0] * n
reached = set()


for ui in range(n):
    if ui + 1 not in reached:
        dfs(v, ui)

for ui in range(n):
    print('%d %d %d' % (ui + 1, d[ui], f[ui]))
