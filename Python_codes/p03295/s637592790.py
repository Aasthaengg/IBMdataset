n, m = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(m)]
line.sort(key=lambda x: x[1])

ans = 1
now = line[0][1]
for s, g in line[1:]:
    if s >= now:
        ans += 1
        now = g
print(ans)
