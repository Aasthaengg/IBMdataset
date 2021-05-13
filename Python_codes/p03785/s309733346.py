N, C, K = map(int, input().split())
p = 0
bus = 0
time = 0
b = sorted([int(input()) for i in range(N)])
for i in range(N):
    a = b[i]
    if a - time > K or p == C:
        p = 0
    if p == 0:
        time = a
        bus += 1
    p += 1
print(bus)