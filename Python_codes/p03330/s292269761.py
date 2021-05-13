from collections import Counter
import itertools
N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]


m0 = Counter()
c0 = 0
m1 = Counter()
c1 = 0
m2 = Counter()
c2 = 0
for i in range(N):
    for j in range(N):
        if ((i+1)+(j+1)) % 3 == 0:
            m0[c[i][j]] += 1
            c0 += 1
        elif ((i+1)+(j+1)) % 3 == 1:
            m1[c[i][j]] += 1
            c1 += 1
        else:
            m2[c[i][j]] += 1
            c2 += 1

m = [m0, m1, m2]
cnt = [c0, c1, c2]

ans = float('inf')
for perm in itertools.permutations([i for i in range(1, C+1)], 3):
    tmp = 0
    for i in range(3):
        for k, v in m[i].items():
            if k != perm[i]:
                tmp += D[k-1][perm[i]-1] * v
    ans = min(ans, tmp)
print(ans)