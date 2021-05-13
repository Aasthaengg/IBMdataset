
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

d = {}
for st in s:
    if st not in d:
        d[st] = 0
    d[st] += 1
for st in t:
    if st not in d:
        d[st] = 0
    d[st] -= 1

print(max(0, max(d.values())))
