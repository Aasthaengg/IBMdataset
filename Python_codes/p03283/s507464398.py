import sys
import io, os
#input = sys.stdin.buffer.readline
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, m, Q = map(int, input().split())
C = [[0]*n for _ in range(n)]
for i in range(m):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    C[l][r] += 1

s = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + C[i][j]

for i in range(Q):
    p, q = map(int, input().split())
    p, q = p-1, q-1
    ans = s[q+1][q+1]-s[q+1][p]-s[p][q+1]+s[p][p]
    print(ans)
