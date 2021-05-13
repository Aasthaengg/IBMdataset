def main():
    n = int(input())
    x = input()

    c1 = x.count('1')
    c1p, c1m = c1 + 1, c1 - 1
    sp = sum(pow(2, n - i - 1, c1p) for i, c in enumerate(x) if c == '1')
    sm = None
    if c1m > 0:
        sm = sum(pow(2, n - i - 1, c1m) for i, c in enumerate(x) if c == '1')

    A = [0] * n
    for i in range(n):
        nx = None
        if x[i] == '0':
            nx = (sp + pow(2, n - i - 1, c1p)) % c1p
        else:
            if sm is None:
                continue

            nx = (sm - pow(2, n - i - 1, c1m)) % c1m

        A[i] += 1

        while nx > 0:
            nx %= format(nx, 'b').count('1')
            A[i] += 1

    for a in A:
        print(a)


if __name__ == '__main__':
    main()
