N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

in_bus = 0
first = 0
last = 0
bus_count = 0
for i in range(N):
    if (i == 0):
        first = T[i]
        last = T[i] + K
        in_bus += 1
        bus_count += 1
        continue

    if (in_bus == C):
        bus_count += 1
        in_bus = 1
        first = T[i]
        last = T[i] + K
        continue

    if (T[i] >= first and last >= T[i]):
        in_bus += 1
    else:
        first = T[i]
        last = T[i] + K
        in_bus = 1
        bus_count += 1


print(bus_count)
