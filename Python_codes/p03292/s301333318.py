import itertools

a = map(int, input().split())
ans = 1000000000000000
for p in itertools.permutations(a):

    cost = 0
    for i in range(1, len(p)):
        cost += abs(p[i] - p[i - 1])
    if ans >= cost:
        ans = cost

print(ans)
