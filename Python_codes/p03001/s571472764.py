def solve(w, h, x, y):
    #   h|-----|--|
    #    |-----|--|
    #    |-----|--|
    #   y|-----o--|
    #    |-----|--|
    #    0     x  w

    is_multi = (x == w/2) and (y == h/2)
    return "{:05f}".format(float((h * w)/2)), is_multi


if __name__ == '__main__':
    w, h, x, y = map(int, input().split())
    area, is_multi = solve(w, h, x, y)
    print(area, int(is_multi))
