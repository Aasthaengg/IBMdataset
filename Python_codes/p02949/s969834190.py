n, m, p = map(int, input().split())
abc = []
for _ in range(m):
    a, b, c = map(int, input().split())
    abc.append([a-1, b-1, p-c])

d = [float('inf')] * n
d[0] = 0

for i in range(n):
    for a, b, c in abc:
        d[b] = min(d[b], d[a] + c)

for a, b, c in abc:
    if d[b] > d[a] + c:
        d[b] = - float('inf')

for i in range(n):
    for a, b, c in abc:
        d[b] = min(d[b], d[a] + c)

if d[n-1] == - float('inf'):
    print(-1)
else:
    print(max(0, - d[n-1]))
