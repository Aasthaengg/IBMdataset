import itertools

N, *D = map(int, open(0).read().split())
ans = 0
for v in itertools.combinations(D, 2):
    ans += v[0] * v[1]

print(ans)