n, d = map(int, input().split())
d2 = d ** 2

res = 0
for _ in range(n):
    x, y = map(int, input().split())
    if d2 >= x**2 + y**2:
        res += 1

print(res)
