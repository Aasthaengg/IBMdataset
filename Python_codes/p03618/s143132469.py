import math

a = input()

d = {}

for ai in a:
    if ai in d:
        d[ai] += 1
    else:
        d[ai] = 1

ans = len(a) * (len(a) -1) // 2 + 1

for k in d:
    ans -= d[k] * (d[k] -1) // 2
print(ans)
