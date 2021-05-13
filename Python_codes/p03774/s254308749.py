n, m = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(n)]
CP = [list(map(int, input().split())) for _ in range(m)]

for a, b in ST:
    dif, pos = 1e20, 100
    for j, (c, d) in enumerate(CP):
        tmp = abs(a - c) + abs(b - d)
        if dif > tmp:
            dif, pos = tmp, j + 1
    print(pos)