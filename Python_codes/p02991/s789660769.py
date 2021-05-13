n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

g = [set() for _ in range(3 * n)]

for u, v in uv:
    a = u - 1
    b = v - 1
    g[a].add(n + b)
    g[n+a].add(n*2 + b)
    g[n*2+a].add(b)

#print(g)

s -= 1
t -= 1
ans = 0
temp = set()
temp.add(s)
while 1:
    ans += 1
    next = set()
    for x in temp:
        for y in g[x]:
            next.add(y)
        g[x] = []
    if len(next) == 0:
        print(-1)
        exit()
    if t in next:
        print(ans // 3)
        exit()
    temp = next
