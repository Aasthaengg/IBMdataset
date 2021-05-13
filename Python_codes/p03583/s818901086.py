def main():
    N = int(input())

    for n in range(1, 3501):
        for h in range(1, 3501):
            b = 4 * h * n - N * n - N * h
            if b > 0:
                w = N * h * n / b
                if w.is_integer():
                    print("{} {} {}".format(n, h, int(w)))
                    exit()

if __name__ == '__main__':
    main()
