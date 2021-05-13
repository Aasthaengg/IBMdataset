def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    # 何個符号反転できるか？
    # -> 1 ～ N - 1 個反転できる
    # N - 1個: (((v - w) - x) - y) - z
    # N - 2個: ((v - w) - x) - (y - z)
    # ...
    #     2個: (v - w) - ((x - y) - z)
    #     1個: v - (((w - x) - y) - z)
    neg_cnt = sum([1 for a in A if a < 0])
    M = 0
    proc = list()
    if neg_cnt == N:
        # 全部負：絶対値が一番小さいもの以外を全て符号反転
        A.sort(reverse=True)
        x = A[0]
        for y in A[1:]:
            proc.append((x, y))
            x -= y
        M = x
    elif neg_cnt == 0:
        # 全部非負：一番小さいものだけ符号反転
        A.sort()
        x = A[0]
        for y in A[1:-1]:
            proc.append((x, y))
            x -= y
        x, y = A[-1], x
        proc.append((x, y))
        M = x - y
    else:
        # k個が負（1 <= k <= N - 1）：負の値を全て符号反転
        A.sort()
        x = A[-1]
        for y in A[:neg_cnt-1]:
            proc.append((x, y))
            x -= y
        former = x
        x = A[neg_cnt-1]  # the last negative element
        for y in A[neg_cnt:-1]:
            proc.append((x, y))
            x -= y
        latter = x
        proc.append((former, latter))
        M = former - latter
    print(M)
    for p in proc:
        x, y = p
        print('{} {}'.format(x, y))


if __name__ == '__main__':
    main()