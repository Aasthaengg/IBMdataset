N = int(input())
d = {}
for _ in range(N):
    w = input().strip()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
m = max(d.values())
r = []
for k, v in d.items():
    if v == m:
        r.append(k)
for w in sorted(r):
    print(w)
