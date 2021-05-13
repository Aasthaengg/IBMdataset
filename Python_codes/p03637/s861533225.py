def main():
    n, *a = map(int, open(0).read().split())

    o = sum([i % 2 == 1 for i in a])
    p = sum([i % 4 == 0 for i in a])
    q = sum([i % 2 == 0 for i in a]) - p

    if p + 1 >= o and not q:
        print("Yes")
    elif p >= o and q:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
