def main():
    n, *a = map(int, open(0).read().split())
    b = [i for i in a if i <= 0]
    *ab, = map(abs, a)
    c = sum(ab)
    if len(b) % 2 == 0:
        print(c)
    else:
        print(c - 2 * min(ab))


if __name__ == '__main__':
    main()
