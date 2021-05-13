def distance(x, y):
    return (x ** 2 + y ** 2) ** (1 / 2)


def main():
    n, d = map(int, input().split())
    xy_lst = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    for i in range(n):
        x = xy_lst[i][0]
        y = xy_lst[i][1]
        if distance(x, y) <= d:
            count += 1

    print(count)


if __name__ == '__main__':
    main()