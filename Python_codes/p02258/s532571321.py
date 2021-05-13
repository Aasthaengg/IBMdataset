def main():
    n = int(input())

    r  = 0
    ri = 0

    for i in range(n):
        m = int(input())

        if 0 == i:
            ri = m
            continue

        if 1 == i:
            r = m - ri

        r  = max(r, m - ri)
        ri = min(ri, m)

    print(r)

if __name__ == '__main__':
    main()