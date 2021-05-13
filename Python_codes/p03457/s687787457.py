n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]

def func(n, pos):
    c_t, c_x, c_y = 0, 0, 0

    for i in pos:
        d_t = i[0] - c_t
        z = abs(i[1] - c_x) + abs(i[2] - c_y)

        if z > d_t or (d_t - z) % 2 != 0:
            return "No"
        else:
            c_t, c_x, c_y = i[0], i[1], i[2]

    return "Yes"


print(func(n, pos))
