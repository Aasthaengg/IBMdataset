from scipy.spatial import distance


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    op = []
    c = 0

    for y in range(h):
        if y % 2 == 0:
            for x in range(w):
                if (c == 1):
                    a[y][x] += 1
                    c = 0

                if a[y][x] % 2 == 1:
                    c = 1
                    x, y = x + 1, y + 1
                    if (x == w):
                        if y != h:
                            op.append([y, x, y + 1, x])
                        else:
                            break
                    else:
                        op.append([y, x, y, x + 1])
                    x, y = x - 1, y - 1

        else:
            for x in reversed(range(w)):
                if (c == 1):
                    a[y][x] += 1
                    c = 0

                if a[y][x] % 2 == 1:
                    c = 1
                    x, y = x + 1, y + 1
                    if (x == 1):
                        if y != h:
                            op.append([y, x, y + 1, x])
                        else:
                            break
                    else:
                        op.append([y, x, y, x - 1])
                    x, y = x - 1, y - 1

    print(len(op))
    for o in op:
        print(' '.join(map(str, o)))


main()
