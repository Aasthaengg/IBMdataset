n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = {}
for i in range(len(a)):
    if a[i] - 1 in d:
        v = d[a[i] - 1]
        del d[a[i] - 1]
        d[a[i]] = v + 1
    else:
        d[a[i]] = 1
print(len(a) - max(list(d.values())))