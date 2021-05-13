from itertools import permutations
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
count = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        count[(i+j) % 3][c[i][j]] += 1
ans = float('inf')
for p in permutations(range(C), 3):
    tmp = 0
    for i in range(3):
        for j in range(C):
            tmp += count[i][j] * D[j][p[i]]
    ans = min(ans, tmp)
print(ans)
