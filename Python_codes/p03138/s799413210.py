def main():
    N, K = map(int, input().split())
    *A, = map(int, input().split())

    ctr = [0] * 60

    for x in A:
        *bit, = map(int, bin(x)[2:])
        bit.reverse()
        for j, b in enumerate(bit):
            i = (60 - 1) - j
            ctr[i] += b

    ans = 0
    d = 1 << (60 - 1)
    x = 0
    for j, cnt in enumerate(ctr):
        if (cnt < N - cnt) and (x + d <= K):  # フラグを立てた方が得する
            x += d
            ans += (N - cnt) * d
        else:
            ans += cnt * d
        d >>= 1
    print(ans)


if __name__ == '__main__':
    main()
