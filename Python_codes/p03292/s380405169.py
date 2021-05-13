import itertools
a1, a2, a3 = map(int, input().split())
ans = 10 ** 9
for v in itertools.permutations([a1, a2, a3]):
    d = 0
    for i in range(1, 3):
        d += abs(v[i]-v[i-1])
    ans = min(ans, d)

print(ans)
