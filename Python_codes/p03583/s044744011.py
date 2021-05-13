import sys
input = sys.stdin.readline


def main():
    N = int(input())
    for h in range(1, 3501):
        for n in range(1, 3501):
            d = 4*h*n - n*N - h*N
            if d > 0:
                w = N*h*n / d
                if w.is_integer():
                    print(h, n, int(w))
                    return


if __name__ == '__main__':
    main()
