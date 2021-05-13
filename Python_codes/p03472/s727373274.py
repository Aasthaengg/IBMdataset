n, h = map(int, input().split())
a = [0]*n
b = [0]*n
maxa = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())
    maxa = max(maxa, a[i])

c = []
for i in range(n):
    if b[i] >= maxa:
        c.append(b[i])
        
c.sort()
csum = sum(c)
count = len(c)

if csum >= h:
    i = 0
    while csum - c[i] >= h:
        if i == len(c):
            break
        else:
            csum -= c[i]
            i += 1
            count -= 1
else:
    if (h - csum) % maxa == 0:
        count += (h - csum) // maxa
    else:
        count += (h - csum) // maxa
        count += 1

print(count)