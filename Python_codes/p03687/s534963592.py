s = input()
d = {}
ans = float("inf")
for i, a in enumerate(s):
    if a not in d:
        d[a] = [i + 1]
    else:
        d[a].append(i + 1)
for k in d.keys():
    c = 0
    for i in range(1, len(d[k])):
        c = max(c, d[k][i] - d[k][i - 1] - 1)
    ans = min(ans, max(c, d[k][0] - 1, len(s) - d[k][-1]))
print(ans)