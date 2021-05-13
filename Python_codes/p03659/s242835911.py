def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    tot = sum(A)

    ans = (10 ** 9) * (2 * 10 ** 5) + 1
    s = 0
    for x in A[:-1]:
        s += x + x
        diff = abs(tot - s)
        if ans > diff:
            ans = diff

    print(ans)


if __name__ == '__main__':
    main()
