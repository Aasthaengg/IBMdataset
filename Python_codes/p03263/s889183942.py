import sys

input = sys.stdin.readline


def calc_next_hw(H, W, h, w):
    # -->
    if h % 2 == 0:
        if w == W - 1:
            next_h = h + 1
            next_w = W - 1
        else:
            next_h = h
            next_w = w + 1
    # <--
    else:
        if w == 0:
            next_h = h + 1
            next_w = 0
        else:
            next_h = h
            next_w = w - 1
    return next_h, next_w


def main():
    H, W = map(int, input().split())
    a = [None] * H
    for i in range(H):
        a[i] = list(map(int, input().split()))

    ans = []
    h, w, = 0, 0
    next_h, next_w = 0, 0
    for _ in range(H * W - 1):
        next_h, next_w = calc_next_hw(H, W, h, w)
        if a[h][w] % 2 == 1:
            a[h][w] -= 1
            a[next_h][next_w] += 1
            ans.append((h + 1, w + 1, next_h + 1, next_w + 1))
        h, w = next_h, next_w

    print(len(ans))
    for xyxy in ans:
        print(*xyxy)


if __name__ == "__main__":
    main()
