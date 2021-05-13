def main():
    N, M = (int(i) for i in input().split())
    S = input()
    T = input()

    def gcd(x, y):
        if y == 0:
            return x
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x*y//gcd(x, y)
    L = lcm(N, M)

    match = lcm(L//N, L//M)
    for a in range(0, L, match):
        if S[a * N//L] != T[a * M//L]:
            return print(-1)
    else:
        print(L)


if __name__ == '__main__':
    main()
