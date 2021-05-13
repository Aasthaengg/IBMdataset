n, c, k = map(int, input().split())
T = sorted([int(input()) for _ in range(n)])

limit = T[0] + k
bus = [0]
ans = 0
for t in T:
    if t <= limit:
        if bus[-1] < c:
            bus[-1] += 1
        else:
            bus.append(1)
            limit = t + k

    else:
        limit = t + k
        ans += len(bus)
        bus = [1]

ans += len(bus)

print(ans)