n,k = map(int,input().split())
p = [int(i)-1 for i in input().split()]
c = [int(i) for i in input().split()]
INF = float("INF")
ans = -INF

for si in range(n):
    x = si
    S = []
    tot = 0
    while True:
        x = p[x]
        S.append(c[x])
        tot += c[x]
        if x == si: break
    l = len(S)
    t = 0
    for i in range(l):
        if i+1 > k: break
        t += S[i]
        now = t
        if tot > 0:
            e = (k-(i+1))//l
            now += tot*e
        ans = max(ans, now)
print(ans)