h, w, n = map(int, input().split())

if n == 0:
    print((h-2) * (w-2))
    for i in range(9):
        print(0)
    exit()

ab = [tuple(int(x) - 1 for x in input().split()) for _ in range(n)]

p = []

for a, b in ab:
    for x in range(max(0, a-2), min(h-3, a) + 1):
        for y in range(max(0, b-2), min(w-3, b) + 1):
            p.append([x, y])

p.sort()

#print(p)

ans = [0] * 10

c = 1
for i in range(len(p) - 1):
    if p[i] == p[i + 1]:
        c += 1
    else:
        ans[c] += 1
        c = 1
ans[c] += 1

ans[0] = (h - 2) * (w - 2) - sum(ans[1:])

for i in range(10):
    print(ans[i])