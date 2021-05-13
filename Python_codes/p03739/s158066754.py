n = int(input())
a = list(map(int, input().split()))

c1 = 0
s = 0

for i in range(n):
    s += a[i]
    if i % 2 == 1:
        if s <= 0:
            c1 += 1 - s
            s = 1

    else: 
        if s >= 0:
            c1 += 1 + s
            s = -1

c2 = 0
t = 0

for i in range(n):
    t += a[i]
    if i % 2 == 1:
        if t >= 0:
            c2 += 1 + t
            t = -1
    else:
        if t <= 0:
            c2 += 1 - t
            t = 1

print(min(c1, c2))
