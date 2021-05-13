def main():
    A, B = list(map(int, input().split(' ')))
    A -= 1
    B -= 1
    K = 50
    H, W = 2 * K, 2 * K
    ans = list()
    for h in range(K):
        if h % 2 == 0:
            ans.append('#' * W)
        else:
            white_cells = K if A >= K else max([A, 0])
            ans.append('#.' * white_cells + '##' * (K - white_cells))
            A -= white_cells
    for h in range(K):
        if h % 2 == 0:
            ans.append('.' * W)
        else:
            black_cells = K if B >= K else max([B, 0])
            ans.append('.#' * black_cells + '..' * (K - black_cells))
            B -= black_cells
    print('{} {}'.format(H, W))
    for s in ans:
        print(s)


if __name__ == '__main__':
    main()
