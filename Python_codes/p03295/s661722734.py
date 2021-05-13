n, m  =map(int, input().split())

routes = []

for i in range(m):
    a,b = map(int, input().split())
    routes.append([a,b])

routes.sort(key=lambda x: x[1])

cut = 0
ans = 0

for route in routes:
    if route[0] >= cut:
        cut = route[1]
        ans += 1

print(ans)