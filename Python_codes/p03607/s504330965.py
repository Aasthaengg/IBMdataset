n = int(input())

d = dict()
for _ in range(n):
    a = int(input())
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

res = 0
for v in d.values():
    if v % 2 == 1:
        res += 1

print(res)