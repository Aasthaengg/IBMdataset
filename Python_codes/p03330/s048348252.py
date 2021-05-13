import itertools
import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
inpl = lambda: list(map(int,input().split()))

N, C = inpl()
D = [inpl() for _ in range(C)]
c = [inpl() for _ in range(N)]

nc = [[0]*C for _ in range(3)]
for i in range(N):
    for j in range(N):
        nc[(i+j)%3][c[i][j]-1] += 1

strangeness = [[sum(nc[k][oldc] * D[oldc][newc] for oldc in range(C))
                for newc in range(C)] for k in range(3)]
ans = 1000 * N * N
for xyz in itertools.product(range(C),repeat=3):
    x, y, z = xyz
    if x != y and y != z and z != x:
        s = sum(strangeness[k][xyz[k]] for k in range(3))
        if s < ans:
            ans = s
print(ans)