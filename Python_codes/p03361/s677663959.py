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
    s = [list(map(str, in_s())) for _ in range(H)]

    m = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = 'Yes'
    for y in range(H):
        for x in range(W):
            if s[y][x] == '#':
                for px, py in m:
                    nx = x + px
                    ny = y + py
                    if 0 <= nx < W and 0 <= ny < H:
                        if s[ny][nx] == '#':
                            break
                else:
                    ans = 'No'
                    break

    print(ans)


if __name__ == '__main__':
    main()
