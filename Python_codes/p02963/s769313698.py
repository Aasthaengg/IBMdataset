def agc036_a():
    S = int(input())
    x1 = y1 = 0
    x2 = 10**9
    y2 = 1
    d, m = divmod(S, x2)
    if m == 0:
        y2 = x3 = 0
        y3 = d
    else:
        x3 = x2 - m
        y3 = d + 1
    ans = [x1, y1, x2, y2, x3, y3]
    print(*ans, sep=' ')

agc036_a()