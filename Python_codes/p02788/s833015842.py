n, d, a = map(int, input().split())
m = [tuple(map(int, input().split())) for _ in range(n)]

m.sort()

x = [s[0] for s in m]
h = [s[1] for s in m]

dh = [0] * (n+1)
dh[0] = h[0]
for i in range(n-1):
    dh[i+1] = h[i+1] - h[i]

import bisect
ans = 0
health = 0
for i in range(n):
    health += dh[i]
    if health > 0:
        count = (health + a - 1) // a
        damage = count * a
        ans += count
        health -= damage
        r = bisect.bisect_right(x, x[i] + 2 * d)
        dh[r] += damage
print(ans)