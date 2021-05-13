n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort()
vectors = set()
for i in range(n-1):
    for j in range(i+1, n):
        xi, yi = xy[i]
        xj, yj = xy[j]
        if xj-xi == 0 and yj-yi == 0:
            continue
        unit_vector = (xj-xi, yj-yi)
        vectors |= {unit_vector}
ans = n
for vector in vectors:
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            xi, yi = xy[i]
            xj, yj = xy[j]
            if vector == (xj-xi, yj-yi):
                cnt += 1
    ans = min(ans, n-cnt)
print(ans)
