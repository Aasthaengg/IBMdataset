import itertools
p, q, r = map(int, input().split())
ans = 10**18
for v in itertools.permutations([p, q, r], 2):
    ans = min(ans, sum(v))
print(ans)
