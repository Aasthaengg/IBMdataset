N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -float("INF")
for bit in range(1, 1 << 10):
    tmp = 0
    for i in range(N):
        c = 0
        for k in range(10):
            if (bit >> k) & 1:
                if F[i][k] == 1:
                    c += 1
        tmp += P[i][c]
    ans = max(ans, tmp)

print(ans)