def main():
    n, m, d = map(int, input().split())

    if n - 2 * d - 1 >= 0:
        p1 = (n-2*d) / n
        p2 = 1 - p1
    else:
        p1 = 0
        p2 = 2 * d / n
    if d == 0:
        ans = p1 * 1 / n + p2 / n
        ans *= (m - 1)
    else:
        ans = p1 * 2 / n + p2 / n
        ans *= (m-1)

    print(ans)


if __name__ == '__main__':
    main()
