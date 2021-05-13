import itertools
p, q, r = map(int, input().split())
mn = 10 ** 9
for v in itertools.combinations([p, q, r], 2):
    mn = min(mn, v[0]+v[1])
print(mn)
