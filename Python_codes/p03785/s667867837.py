N, C, K = map(int, input().split())
T = list(int(input()) for i in range(N))
T.sort()
bus = 1
passenger = 0
limit = T[0] + K
for i in range(N):
    if T[i] <= limit and passenger < C:
        passenger += 1
    else:
        bus += 1
        limit = T[i]+K
        passenger = 1
print(bus)