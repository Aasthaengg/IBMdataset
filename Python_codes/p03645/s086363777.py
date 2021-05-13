n, m = map(int, input().split())
d = {}
c = "IMPOSSIBLE"

for i in range(1,n):
    if i == 1:
        d[i] = []
    else:
        d[i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        d[a].append(b)
    elif d[a] < b:
        d[a] = b

for k in d[1]:
    if d[k] == n:
        c = "POSSIBLE"

print(c)
