N, M = map(int, input().split())
PS = [input().split() for _ in range(M)]
Pena = [0] * (N+1)
pena = 0
ac = 0
for p, s in PS:
    p = int(p)
    if s == "AC":
        if Pena[p] >= 0:
            ac += 1
            pena += Pena[p]
            Pena[p] = -999999999
    else:
        Pena[p] += 1
print(ac, pena)
