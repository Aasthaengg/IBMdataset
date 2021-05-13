mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    for a in range(1, 3501):
        for b in range(1, 3501):
            L = 4*a*b - (a+b)*N
            R = a*b*N
            if L <= 0:
                continue
            if R % L == 0:
                c = R // L
                print(a, b, c)
                exit()


if __name__ == '__main__':
    main()
