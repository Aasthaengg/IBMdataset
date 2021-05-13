mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, P = map(int, input().split())
    A = list(map(int, input().split()))

    odd = 0
    even = 0
    for a in A:
        if a&1:
            odd += 1
        else:
            even += 1
    if P:
        if odd == 0:
            print(0)
        else:
            print(2**(N - 1))
    else:
        if odd == 0:
            print(2**N)
        else:
            print(2**(N - 1))


if __name__ == '__main__':
    main()
