s = str(input())
S = list(set(s))
d = {}
for v in S:
    x = s
    cnt = 0
    while x.count(v) < len(x):
        new_x = [0] * (len(x) - 1)
        for i in range(len(x) - 1):
            if x[i] == v or x[i + 1] == v:
                new_x[i] = v
        cnt += 1
        x = new_x
    d[v] = cnt
print(min(d.values()))
