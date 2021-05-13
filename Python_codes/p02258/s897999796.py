def main():
    n = input()
    d = -999999999

    m = input()
    for i in range(n - 1):
        r = input()
        if (d < r - m):
            d = r - m
        if (m > r):
            m = r
    print(d)

main()