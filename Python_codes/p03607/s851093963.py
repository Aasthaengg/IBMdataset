n = int(input())
d = dict()
for _ in range(n):
    k = int(input())
    if d.get(k) == None or d.get(k) == 0:
        d[k] = 1
    else:
        d[k] = 0

print(sum(d.values()))