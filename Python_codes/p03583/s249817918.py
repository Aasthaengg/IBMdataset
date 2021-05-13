def main():
    N = int(input())
    for h in range(1, 3501):
        denominator = 4*h - N
        numerator = N*h
        if denominator > 0:
            n = (numerator//denominator) + 1
            denominator = 4*h*n - N*(h+n)
            numerator = N*h*n
            if denominator > 0 and numerator % denominator == 0:
                print(h, n, numerator//denominator)
                exit()


if __name__ == "__main__":
    main()
