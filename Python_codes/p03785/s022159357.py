N, C, K = map(int, input().strip().split(" "))
t = sorted([int(input().strip()) for _ in range(N)])

bus = 0
idx = 0
while idx < N:
    bus_go = t[idx] + K
    tmp = 0
    while idx < N:
        if t[idx] <= bus_go:
            tmp += 1
            idx += 1
            if idx == N:
                break
            if tmp == C:
                bus += 1
                tmp = 0
                bus_go = t[idx] + K
        else:
            break
    if tmp > 0:
        bus += 1

print(bus)
