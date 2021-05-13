m, k = map(int, input().split())

if m*k == 1:
    print(-1)
    exit()

if 1 << m <= k:
    print(-1)
    exit()

if k == 0:
    t = []
    for i in range(1 << m):
        for _ in range(2):
            t.append(i)
    print(*t)
    exit()

b = []
for i in range(1 << m):
    if i != k:
        b.append(i)

c = b[::-1]

a = b + [k] + c + [k]
print(*a)
