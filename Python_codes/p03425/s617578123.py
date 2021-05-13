from itertools import combinations as C

d = {}
for _ in range(int(input())):
    s = input()[0]
    d[s] = d.get(s, 0) + 1

dk = set(d.keys()) & set("MARCH")
ans = 0
for p, q, r in C(dk, 3):
    ans += d[p] * d[q] * d[r]
else:
    print(ans)