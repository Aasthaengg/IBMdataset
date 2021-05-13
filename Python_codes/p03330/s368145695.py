n, c = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(c)]
C = [list(map(int, input().split())) for _ in range(n)]
for i, l in enumerate(C):
    l = [x-1 for x in l]
    C[i] = l

X = [[0]*c for _ in range(3)]
for i in range(n):
    for j in range(n):
        r = (i+j)%3
        for k in range(c):
            X[r][k] += D[C[i][j]][k]
import itertools
ans = 10**18
for p in itertools.permutations(range(c), 3):
    temp = 0
    for i in range(3):
        temp += X[i][p[i]]
    ans = min(temp, ans)
print(ans)
