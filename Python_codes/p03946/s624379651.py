def main():
    n, t, *a = map(int, open(0).read().split())
    b = 0
    c = float("Inf")
    d = 0
    for i in range(n):
        x = a[i]
        if x - c > b:
            b = x - c
            d = 1
        elif x - c == b:
            d += 1
        c = min(c, x)

    print(d)


if __name__ == '__main__':
    main()
