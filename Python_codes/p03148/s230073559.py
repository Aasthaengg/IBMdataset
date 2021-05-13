N, K = map(int, input().split())
TD = [tuple(map(int, input().split())) for _ in range(N)]
TD.sort(key=lambda p: -p[1])
neta = set()
oisi = netan = 0
amari = []
for t, d in TD[:K]:
    oisi += d
    if t not in neta:
        neta.add(t)
        netan += 1
    else:
        amari.append(d)
ans = oisi + netan * netan
for t, d in TD[K:]:
    if netan == K or not amari:
        break
    if t not in neta:
        neta.add(t)
        netan += 1
        oisi += d - amari.pop()
        ans = max(ans, oisi + netan * netan)
print(ans)