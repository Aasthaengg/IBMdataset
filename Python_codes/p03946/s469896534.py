def main():
    N, T = map(int, input().split())
    *A, = map(int, input().split())

    mi = A[0]
    d_ma = -1
    cnt = 0
    for x in A:
        d = x - mi
        if d_ma < d:
            d_ma = d
            cnt = 1
        elif d_ma == d:
            cnt += 1
        if mi > x:
            mi = x

    print(cnt)


if __name__ == '__main__':
    main()
