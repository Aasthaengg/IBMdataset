h, w, m = map(int, input().split())
s = []
r = [0] * (h + 1)
c = [0] * (w + 1)
for i in range(m):
    bh, bw = map(int, input().split())
    s.append([bh, bw])
    r[bh] += 1
    c[bw] += 1
R = max(r)
nr = {i for i, x in enumerate(r) if x == R}
C = max(c)
nc = {i for i, x in enumerate(c) if x == C}
count = sum(x in nr and y in nc for x, y in s)
print(R + C - (len(nr) * len(nc) == count))