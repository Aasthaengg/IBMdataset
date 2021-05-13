import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    H, W = in_nn()
    a = [list(map(int, readline().split())) for _ in range(H)]

    odd_count = 0
    for y in range(H):
        for x in range(W):
            if a[y][x] % 2 == 1:
                odd_count += 1

    if odd_count % 2 == 1:
        odd_count -= 1

    count = 0
    x, y = 0, 0
    px, py = -1, -1
    odd_f = False

    ans = []
    while True:

        if odd_f:
            ans.append((py + 1, px + 1, y + 1, x + 1))
            if a[y][x] % 2 == 1:
                odd_f = False
        else:
            if a[y][x] % 2 == 1:
                odd_f = True

        px, py = x, y
        if a[y][x] % 2 == 1:
            count += 1
            if count >= odd_count:
                break

        if y % 2 == 0:
            if x == W - 1:
                y += 1
            else:
                x += 1
        else:
            if x == 0:
                y += 1
            else:
                x -= 1

        if y >= H:
            break

    print(len(ans))
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()
