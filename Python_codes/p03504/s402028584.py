N, C = map(int, input().split())

imos = [0]*(10**5+1)

pgs = []
for _ in range(N):
    s, t, c = map(int, input().split())
    pgs.append((s, t, c))

pgs = sorted(pgs, key=lambda x: (x[2], x[0]))

for i in range(N):
    s, t, c = pgs[i]
    if i >= 1 and pgs[i-1][2] == pgs[i][2] and pgs[i-1][1] == pgs[i][0]:
        imos[s] += 1
        imos[t] -= 1
    else:
        imos[s-1] += 1
        imos[t] -= 1

ans = 0
a = 0
for i in imos:
    a += i
    ans = max(ans, a)

print(ans)
