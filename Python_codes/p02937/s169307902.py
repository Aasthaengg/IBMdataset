from bisect import bisect_left
s = input()
t = input()

n = len(s)
s = s * 2


r = {}
for i, v in enumerate(s):
    if v in r.keys():
        r[v].append(i+1)
    else:
        r[v] = [i+1]

now = 0

lt = len(t)
for v in t:
    if v in r.keys():
        index = bisect_left(r[v], now % n + 1)
        tmp = r[v][index]
        now += tmp - now % n
    else:
        print(-1)
        exit()

print(now)