N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

bus = 1
lastPassenger = T[0]
waiting = 1
for t in T[1:]:
    if waiting < C and lastPassenger + K >= t:
        waiting += 1
    else:
        waiting = 1
        lastPassenger = t
        bus += 1

print(bus)