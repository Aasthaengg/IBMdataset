from collections import Counter
from itertools import permutations
N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
c_field = [list(map(int, input().split())) for i in range(N)]

mod = [[] for _ in range(3)]

for i in range(N):
    for j in range(N):
        mod[(i+j+2)%3].append(c_field[i][j])

for i in range(3):
    mod[i] = Counter(mod[i])

def calc(p):
    ret = 0
    for j in range(3):
        for i, v in mod[j].items():
            if i == p[j]: continue
            ret += D[i-1][p[j]-1] * v
    return ret

ans = 10 ** 30
for p in permutations(range(1,C+1), 3):
    ans = min(ans, calc(p))

print(ans)
