n = int(input())
d = {}
for i in range(n):
    a = int(input())
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
c = 0
for i in d:
    if d[i] % 2 == 1:
        c += 1
print(c)