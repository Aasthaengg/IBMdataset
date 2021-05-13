import math
import bisect
n,d,a = map(int,input().split())
L = []
kyo = []
for i in range(n):
    x,h = map(int,input().split())
    L.append([x,h])
    kyo.append(x)
L.sort()
kyo.sort()
ans = 0
imos = [0]*(n+1)
cur = 0
ran = 2*d
for i in range(n):
    if imos[cur] < L[cur][1]:
        t = int(math.ceil((L[cur][1]-imos[cur])/a))
        ans += t
        imos[cur] += t*a
        lim = bisect.bisect_right(kyo, kyo[cur]+ran)
        imos[lim] -= t*a
    imos[i+1] += imos[i]
    cur += 1
print(ans)
