N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

f = lambda i, j, k, l: abs(i - k) + abs(j - l)

for c_x in range(0, 101):
    for c_y in range(0, 101):
        d = []
        h_max = float("inf")
        for m in info:
            x, y, h = m[0], m[1], m[2]
            if h > 0:
                H = f(x, y, c_x, c_y) + h
                d.append(H)
            else:
                h_max = min(h_max, f(x, y, c_x, c_y))
        else:
            d = list(set(d))
            if len(d) == 1 and 1 <= d[-1] and d[-1] <= h_max:
                print(c_x, c_y, d[-1])
                exit()
