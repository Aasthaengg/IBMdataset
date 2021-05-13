n, m = map(int, input().split())
start = []
for i in range(n):
    a, b = map(int, input().split())
    start.append([a, b])
check = []
for i in range(m):
    c, d = map(int, input().split())
    check.append([c, d])

for a, b in start:
    distance = 1001001001
    ans = 0
    for i in range(len(check)):
        c, d = check[i][0], check[i][1]
        if abs(a - c) + abs(b - d) < distance:
            distance = abs(a - c) + abs(b - d)
            ans = i + 1
    print(ans)
