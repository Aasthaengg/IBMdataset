def koch_curve(n, x1, y1, x2, y2):
    if n == 0:
        return [(x1, y1)]
    s_x = (2 * x1 + x2) / 3
    s_y = (2 * y1 + y2) / 3
    t_x = (x1 + 2 * x2) / 3
    t_y = (y1 + 2 * y2) / 3
    # 回転行列を用いて
    u_x = (t_x - s_x) * .5 - (t_y - s_y) * (3 ** .5 / 2) + s_x
    u_y = (t_x - s_x) * (3 ** .5 / 2) + (t_y - s_y) * .5  + s_y
    ret = koch_curve(n - 1, x1, y1, s_x, s_y) + \
        koch_curve(n - 1, s_x, s_y, u_x, u_y) + \
        koch_curve(n - 1, u_x, u_y, t_x, t_y) + \
        koch_curve(n - 1, t_x, t_y, x2, y2)
    return ret
for x, y in koch_curve(int(input()), 0, 0, 100, 0):
    print('{:.8f} {:.8f}'.format(x, y))
print('{:.8f} {:.8f}'.format(100, 0))
