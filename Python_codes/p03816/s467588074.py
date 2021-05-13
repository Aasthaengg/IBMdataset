def main():
    from collections import Counter
    n, *a = map(int, open(0).read().split())
    s = len(set(a))

    if s % 2 == 1:
        print(s)
    else:
        print(s - 1)


if __name__ == '__main__':
    main()
