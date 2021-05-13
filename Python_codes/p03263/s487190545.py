def main():
    H, W = list(map(int, input().split(' ')))
    a = [list(map(int, input().split(' '))) for _ in range(H)]
    cnt = 0
    history = list()
    for h in range(H):
        for w in range(W - 1):
            if a[h][w] % 2 == 1:
                a[h][w] -= 1
                a[h][w + 1] += 1
                history.append((h + 1, w + 1, h + 1, w + 2))
                cnt += 1
    for h in range(H - 1):
        if a[h][W - 1] % 2 == 1:
            a[h][W - 1] -= 1
            a[h + 1][W - 1] += 1
            history.append((h + 1, W, h + 2, W))
            cnt += 1
    print(cnt)
    for hist in history:
        print(' '.join(map(str, hist)))


if __name__ == '__main__':
    main()