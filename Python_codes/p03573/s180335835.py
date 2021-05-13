d = {}
for i in input().split():
    if d.get(i) is None:
        d[i] = 0
    d[i] += 1
for k, v in d.items():
    if v == 1:
        print(k)
        exit()