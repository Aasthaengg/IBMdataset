print(
    (lambda out: 'No' if out else 'Yes')(
        (lambda w, h, x, y, r: x-r < 0 or w < x+r or \
                               y-r < 0 or h < y+r)(
            *map(int, input().split()))))