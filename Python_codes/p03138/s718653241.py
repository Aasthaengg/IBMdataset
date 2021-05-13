def main():
    N, K = map(int, input().split())
    *A, = map(int, input().split())

    def bit60(x):
        *bit, = map(int, bin(x)[2:])
        zfill = 60 - len(bit)
        ret = [0] * zfill
        ret += bit
        return ret

    # print(*map(bit60, A))

    ctr = [0] * 60
    for bit in map(bit60, A):
        for j in range(60):
            ctr[j] += bit[j]

    ans = 0
    d = 1 << (60 - 1)
    x = 0
    for j in range(60):
        if (ctr[j] < N - ctr[j]) and (x + d <= K):  # フラグを立てた方が得する
            x += d
            ans += (N - ctr[j]) * d
        else:
            ans += ctr[j] * d
        d >>= 1
    print(ans)


if __name__ == '__main__':
    main()
