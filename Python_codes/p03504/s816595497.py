from collections import defaultdict

N, C = map(int, input().split())

D = defaultdict(list)
for _ in range(N):
    s, t, c = map(int, input().split())
    D[c-1].append((s, t))

IMOS = [0]*(10**5+2)
for c in range(C):
    D[c].sort(key=lambda x: x[0])

    pt = -1
    for i, (s, t) in enumerate(D[c]):
        if s == pt:
            IMOS[s+1] += 1
            IMOS[t] -= 1
        else:
            IMOS[s-1] += 1
            IMOS[t] -= 1
        pt = t

ans = 0
a = 0
for i in IMOS:
    a += i
    ans = max(ans, a)

print(ans)
