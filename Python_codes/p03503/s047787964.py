import sys
readline = sys.stdin.readline

N = int(readline())
F = [list(map(int, readline().split())) for _ in range(N)]
P = [list(map(int, readline().split())) for _ in range(N)]

ans = -10**18
for S in range(1, 1<<10):
    res = 0
    for i in range(N):
        cnt = 0
        for j in range(10):
            if (1<<j) & S and F[i][j]:
                cnt += 1
        res += P[i][cnt]

    ans = max(ans, res)

print(ans)