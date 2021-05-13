N,C,K = map(int,input().split())

T = sorted(int(input()) for _ in range(N))


i = 0
bus = 0
while i < N:
    bus += 1
    c = 0
    limit = T[i]+K
    while c < C and i < N and T[i] <= limit:
        c += 1
        i += 1

print(bus)