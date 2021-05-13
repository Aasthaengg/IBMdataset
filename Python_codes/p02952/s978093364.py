
def fn(i):
    return (1 <= i and i <= 9) or (100 <= i and i <= 999) or (10000 <= i and i <= 99999)


def main():
    n = int(input())
    x = range(n + 1)[1:]
    x = tuple(filter(fn, x))

    print(len(x))


if __name__ == '__main__':
    main()
