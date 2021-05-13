N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])
# print(f'{T=}, {C=}, {K=}')

time = T[0] + K
bus = 1
people = 1
# print(f't={T[0]}, {time=}, {bus=}, {people=}')
for t in T[1:]:
    if t <= time and people < C:
        people += 1
    else:
        time = t + K
        bus += 1
        people = 1
    # print(f'{t=}, {time=}, {bus=}, {people=}')
print(bus)
