n, k = map(int, input().split())
a = list(map(int, input().split()))

d = dict()
for v in a:
    if v not in d:
        d[v] = 1
    else:
        d[v] += 1

l = []
for v in d.values():
    l.append(v)
l.sort()

print(sum(l[:len(l)-k]))