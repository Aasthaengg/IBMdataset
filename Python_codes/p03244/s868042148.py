from collections import Counter
d = [Counter(), Counter()]
n = int(input())
v = list(map(int, input().split()))
for i, vi in enumerate(v):
    d[i&1][vi] += 1
a = []
for i in range(2):
    a.append(sorted(d[i].keys(), key=lambda k: d[i][k], reverse=True))
c = [ai[:2] for ai in a]
if len(c[0]) == len(c[1]) == 1 and c[0][0] == c[1][0]:
    print(n // 2)
else:
    ans = 1001001001
    for ci in c[0]:
        for cj in c[1]:
            if ci == cj:
                continue
            cnt = sum(v for k, v in d[0].items() if k != ci) + sum(v for k, v in d[1].items() if k != cj)
            ans = min(ans, cnt)
    print(ans)
