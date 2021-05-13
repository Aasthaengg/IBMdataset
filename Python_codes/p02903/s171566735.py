import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    H, W, A, B = in_nn()

    ans = [[0 for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if 0 <= x < A and 0 <= y < B:
                ans[y][x] = 0
            elif A <= x < W and B <= y < H:
                ans[y][x] = 0
            else:
                ans[y][x] = 1

    for i in range(H):
        print(''.join(map(str, ans[i])))


if __name__ == '__main__':
    main()
