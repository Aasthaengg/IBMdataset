h, w, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

d = dict()
for i in range(len(ab)):
    a = ab[i][0] - 1
    b = ab[i][0] - 1
    d[a] = set()

dp = [0] * 10
dp[0] = (h - 2) * (w - 2)
for i in range(n):
    a = ab[i][0] - 1
    b = ab[i][1] - 1
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = a + dx, b + dy # center
            if nx >= 1 and nx <= h - 2 and ny >= 1 and ny <= w - 2:
                # print(nx, ny)
                tmp = 0
                for dx2 in [-1, 0, 1]:
                    for dy2 in [-1, 0, 1]:
                        if nx + dx2 in d and ny + dy2 in d[nx + dx2]:
                            tmp += 1

                dp[tmp] -= 1
                dp[tmp + 1] += 1

    d[a].add(b)

for x in dp:
    print(x)
