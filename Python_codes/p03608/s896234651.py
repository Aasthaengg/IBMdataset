import sys
input = sys.stdin.readline
from itertools import permutations

def warshall_floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
d = [[10**18]*N for _ in range(N)]

for i in range(N):
    d[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    d[A-1][B-1] = C
    d[B-1][A-1] = C

warshall_floyd()
ans = 10**18

for p in permutations(r):
    now = p[0]-1
    cand = 0

    for i in range(1, R):
        cand += d[now][p[i]-1]
        now = p[i]-1

    ans = min(ans, cand)

print(ans)