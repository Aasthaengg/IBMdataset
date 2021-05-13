def main():
    N = int(input())
    for h in range(1, 3501):
        for n in range(1, 3501):
            denominator = 4*h*n - N*n - N*h
            if denominator <= 0:
                continue
            w = (N*h*n)/denominator
            if w % 1 == 0:
                print(h, n, int(w))
                exit()


if __name__ == "__main__":
    main()
