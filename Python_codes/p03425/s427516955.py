from itertools import combinations

n = int(input())
d = dict({'M':0, 'A':0, 'R':0, 'C':0, 'H':0})
for i in range(n):
    f = input()[0]
    if f in d:
        d[f] += 1

ans = 0
for a, b, c in list(combinations(d.keys(), 3)):
    ans += (d[a] * d[b] * d[c])

print(ans)