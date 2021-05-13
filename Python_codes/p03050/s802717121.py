def main():
    N = int(input())
    # r == N % m == N // m の時、
    # N = r * m + r = r * (m + 1) と書ける(0 < r < m)。
    # Nを2つの正の整数に分解し、上記を満たすmを求めて総和を求める。
    ans = 0
    r = 0
    while (r + 1) ** 2 <= N:
        r += 1
        if N % r > 0:
            continue
        m = N // r - 1
        if r < m:
            ans += m
    print(ans)


if __name__ == '__main__':
    main()