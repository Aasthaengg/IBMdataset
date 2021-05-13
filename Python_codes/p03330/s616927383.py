from collections import Counter
from itertools import permutations
N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
c_field = [list(map(int, input().split())) for i in range(N)]

mod0 = []
mod1 = []
mod2 = []

for i in range(N):
    for j in range(N):
        if (i+j+2) % 3 == 0:
            mod0.append(c_field[i][j])
        elif (i+j+1) % 3 == 1:
            mod1.append(c_field[i][j])
        else:
            mod2.append(c_field[i][j])

mod0 = Counter(mod0)
mod1 = Counter(mod1)
mod2 = Counter(mod2)

def calc(p):
    ret = 0
    for i, v in mod0.items():
        if i == p[0]: continue
        ret += D[i-1][p[0]-1] * v
    for i, v in mod1.items():
        if i == p[1]: continue
        ret += D[i-1][p[1]-1] * v
    for i, v in mod2.items():
        if i == p[2]: continue
        ret += D[i-1][p[2]-1] * v
    return ret
    

ans = 10 ** 30
for p in permutations(range(1,C+1), 3):
    ans = min(ans, calc(p))

print(ans)
