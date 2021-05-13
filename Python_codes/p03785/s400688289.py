n, c, k = map(int, input().split())
arrivals = {}
for _ in range(n):
    t = int(input())
    if t in arrivals:
        arrivals[t] += 1
    else:
        arrivals[t] = 1
data = sorted(arrivals.keys())
ans = 0
current_bus_seats = c
bus_wait_from = data[0]
for time in data:
    ppl = arrivals[time]
    if current_bus_seats != c:
        if time - bus_wait_from > k:
            ans += 1
        else:
            if ppl <= current_bus_seats:
                current_bus_seats -= ppl
                continue
            else:
                ppl -= current_bus_seats
                ans += 1
    current_bus_seats = c
    bus_wait_from = time
    d, m = divmod(ppl, c)
    ans += d
    current_bus_seats -= m
if current_bus_seats < c:
    ans += 1
print(ans)

