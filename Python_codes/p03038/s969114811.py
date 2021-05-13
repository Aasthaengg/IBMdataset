n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

cb = []
for i in range(m):
    b, c = map(int, input().split())
    cb.append([c, b])
cb = list(reversed(sorted(cb)))

c, b = 0, 0
for i in range(n):
    if b <= 0:
        if len(cb) == 0:
            break
        c, b = cb.pop(0)
    if c <= a[i]:
        break
    a[i] = c
    b -= 1
print(sum(a))
