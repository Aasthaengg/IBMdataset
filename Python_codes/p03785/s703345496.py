N, C, K = map(int, input().split())
T = sorted(list(int(input()) for _ in range(N)))

bus = 0
pa = 1
S = T[0]

for i in T[1:]:
    pa += 1
    if K < i-S or pa > C:
        bus += 1
        pa = 1
        S = i
print(bus+1)