n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = set(a)
if k >= len(b):
    print(0)
else:
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    c = list(d.values())
    c.sort()
    e = 0
    for i in range(len(b) - k):
        e += c[i]
    print(e)