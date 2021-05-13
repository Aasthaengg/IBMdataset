def main():
    N = int(input())

    for h in range(1, 3501):
        for n in range(h, 3501):
            if (4*h*n - N*h - N*n)>0 and N*h*n % (4*h*n - N*h - N*n)==0:
                w = N*h*n // (4*h*n - N*h - N*n)
                print(h, n, w)
                exit()

if __name__ == "__main__":
    main()