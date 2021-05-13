def main():
    N = int(input())
    # 4hnw = N(hn + nw + wh)
    # (4hn - N(n + h)) w = Nhn
    for h in range(1, 3501):
        for n in range(1, 3501):
            d = 4 * h * n - N * (n + h)
            if d <= 0 or (N * h * n) % d != 0 or (N * h * n) // d > 3500:
                continue
            w = (N * h * n) // d
            print(h, n, w)
            return


if __name__ == '__main__':
    main()
