D, G = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(D)]
G /= 100
C = 2e3
N = len(pc)
for i in range(2 ** N):
    p = 0
    c = 0
    for j in range(N):
        if i >> j & 1:
            p += pc[j][0] * (j + 1) + pc[j][1] / 100
            c += pc[j][0]
    if p >= G:
        C = min(c, C)
        continue
    for j in range(N-1, -1, -1):
        if not i >> j & 1:
            for k in range(pc[j][0] - 1):
                p += j + 1
                c += 1
                if p >= G:
                    break
        if p >= G:
            break
    if p >= G:
        C = min(c, C)
        continue

print(C)