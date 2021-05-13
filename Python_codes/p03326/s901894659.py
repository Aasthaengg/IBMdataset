n, m = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
from itertools import product
for p in product([-1, 1], repeat=3):
    xyz_ = map(lambda l: l[0]*p[0] + l[1]*p[1] + l[2]*p[2], xyz)
    xyz_ = sorted(xyz_, reverse=True)
    ans = max(ans, sum(xyz_[:m]))
print(ans)
