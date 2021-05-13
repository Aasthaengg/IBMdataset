from collections import Counter
n = int(input())
v = list(map(int, input().split()))
ev = Counter([v[i] for i in range(0, n, 2)])
od = Counter([v[i] for i in range(1, n, 2)])
evk = list(ev.keys())
odk = list(od.keys())
ev_key = evk[0]
for k in evk:
    if ev[k] > ev[ev_key]:
        ev_key = k
od_key = odk[0]
for k in odk:
    if od[k] > od[od_key]:
        od_key = k
evv = list(ev.values()) + [0]
evv.sort(reverse = True)
odv = list(od.values()) + [0]
odv.sort(reverse = True)

if ev_key != od_key:
    print(n - evv[0] - odv[0])
else:
    print(min(n - evv[0] - odv[1], n - evv[1] - odv[0]))