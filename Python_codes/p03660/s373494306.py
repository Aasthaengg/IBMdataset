n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
s = [0]
d1 = [-1] * n
d1[0] = 0
while s:
    d = s.pop()
    for node in g[d]:
        if d1[node] == -1:
            s.append(node)
            d1[node] = d1[d] + 1
s = [n - 1]
d2 = [-1] * n
d2[n - 1] = 0
while s:
    d = s.pop()
    for node in g[d]:
        if d2[node] == -1:
            s.append(node)
            d2[node] = d2[d] + 1
f, s = 0, 0
for i in range(n):
    if d1[i] <= d2[i]:
        f += 1
    else:
        s += 1
if f > s:
    print('Fennec')
else:
    print('Snuke')
