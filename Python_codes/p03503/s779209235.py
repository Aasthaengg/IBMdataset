N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -float("INF")
for bit in range(1 << 10):
    day = []
    for i in range(10):
        if (bit >> i) & 1:
            day.append(i)
    if day == [] or bit == 0:
        continue
    tmp = 0
    for i in range(N):
        c = 0
        for k in day:
            if F[i][k] == 1:
                c += 1
        tmp += P[i][c]
    ans = max(ans, tmp)

print(ans)