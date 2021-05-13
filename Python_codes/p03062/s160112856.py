def main():
    n, *a = map(int, open(0).read().split())
    b = [i for i in a if i <= 0]
    *ab, = map(lambda x: abs(x), a)
    c, d = sum(a), sum(b)
    if len(b) % 2 == 0:
        print(c - 2 * d)
    else:
        print(c - 2 * d - 2 * min(ab))


if __name__ == '__main__':
    main()
