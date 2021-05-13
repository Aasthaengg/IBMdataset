def bitCount(bits):
    bits = (bits & 0x55555555) + (bits >> 1 & 0x55555555)
    bits = (bits & 0x33333333) + (bits >> 2 & 0x33333333)
    bits = (bits & 0x0f0f0f0f) + (bits >> 4 & 0x0f0f0f0f)
    bits = (bits & 0x00ff00ff) + (bits >> 8 & 0x00ff00ff)
    return (bits & 0x0000ffff) + (bits >> 16 & 0x0000ffff)


N = int(input())
F = [0] * N
for i in range(N):
    F[i] = int("".join(input().split()), 2)

P = [] * N
for i in range(N):
    P.append(list(map(int, input().split())))

maxx = -9999999999999999
for bina in range(1, 2**10):
    total = 0
    for i in range(N):
        zyu = bina & F[i]
        total += P[i][bitCount(zyu)]
    maxx = max(total, maxx)

print(maxx)