import heapq

n, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]
grid = [list(map(int, input().split())) for _ in range(n)]

MAXN = 500
MAXC = 30

s = [[0 for _ in range(MAXC)] for _ in range(3)]
for i in range(3):
    for co in range(c):
        for x in range(n):
            for y in range(n):
                if (x+y)%3 == i:
                    s[i][co] += d[grid[x][y]-1][co]

ans = 10**10
for c0 in range(c):
    for c1 in range(c):
        if c0 == c1:
            continue
        for c2 in range(c):
            if c0 == c2 or c1 == c2:
                continue
            ans = min(ans, s[0][c0]+s[1][c1]+s[2][c2])
print(ans)
