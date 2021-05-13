n, y = map(int, input().split())

stop = n + 1
for m in range(stop):
    for g in range(stop - m):
        s = n - m - g
        if y == 10000 * m + 5000 * g + 1000 * s:
            print(m, g, s, sep=" ")
            break
    else:
        continue
    break
else:
    print("-1 -1 -1")