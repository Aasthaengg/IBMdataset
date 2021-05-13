n, m = map(int, input().split())
h = []
for i in range(m):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    h.append((a,b))
h = sorted(h, key=lambda x: (x[0], x[1]))
r = 0
l = 0
cnt = 0
for a, b in h:
    if a >= r:
        cnt += 1
        l = a
        r = b
    elif b < r:
        r = b
    else:
        continue        
print(cnt)