n = int(input())
s = [input() for _ in range(n)]

d = {}
for si in s:
    if si not in d:
        d[si] = 0
    d[si] += 1

s_list = list(sorted(list(d.keys())))
value = max(d.values())
for si in s_list:
    if d[si] == value:
        print(si)
