x = int(input())
D = []
for i in range(x):
    d = int(input())
    D.append(d)
k = []
count = 1
d = max(D)
k.append(d)
D.remove(d)
for j in range(x-1):
    c = max(D)
    if c < d:
        k.append(c)
        d = c
        count += 1
    D.remove(c)

print(count)