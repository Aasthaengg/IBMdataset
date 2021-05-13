from itertools import product

n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for e in product([1, -1], [1, -1], [1, -1]):
    xyz.sort(key=lambda v: (v[0] * e[0]) + (v[1] * e[1]) + (v[2] * e[2]))
    tmp = xyz[:m]
    ans = max(ans, abs(sum([e[0] for e in tmp])) + abs(sum([e[1] for e in tmp])) + abs(sum([e[2] for e in tmp])))
print(ans)
