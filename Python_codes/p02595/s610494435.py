n, d = map(int, input().split())
r = [list(map(int, input().split())) for i in range(n)]
x = 0
for i in range(n):
    if (r[i][0] ** 2) + (r[i][1] ** 2) <= d ** 2:
        x += 1
print(x)