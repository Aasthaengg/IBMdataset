n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]

l.sort(key=lambda x: x[1])

res = 0
pos = 0
for a, b in l:
    if (a - pos) * (b - pos) > 0:
        res += 1
        pos = b - 0.5

print(res)