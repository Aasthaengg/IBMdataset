def main():
    # n行分・m列分ボタンを押すと
    # n(M - m) + m(N - n) = nM + Nm - 2mn マスが黒くなる
    N, M, K = map(int, input().split())
    for n in range(N + 1):
        for m in range(M + 1):
            black = n * (M - m) + (N - n) * m
            if black == K:
                print('Yes')
                return
    print('No')


if __name__ == '__main__':
    main()