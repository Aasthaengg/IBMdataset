def solve():
    H, W = map(int, input().split())
    h, w = map(int, input().split())

    n_all = H * W
    print(n_all - (h * W + w * H) + (h * w))


if __name__ == '__main__':
    solve()