import sys

def dfs(i):
    global V, t, d, f

    if d[i] != 0:
        return

    d[i] = t
    t += 1
    for v in V[i]:
        dfs(v)

    f[i] = t
    t += 1

    return

lines = sys.stdin.readlines()
n = int(lines[0])
V = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    v = map(int, lines[i].split())
    V[v[0]] = v[2:]
d = [0] * (n + 1)
f = [0] * (n + 1)
t = 1

flag = True
while flag:
    flag = False
    for i in range(1, n + 1):
        if d[i] == 0:
            dfs(i)
            flag = True
            break

for i in range(1, n + 1):
    print i, d[i], f[i]