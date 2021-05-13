import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W = map(int, readline().split())
    S = [list(readline().strip()) for _ in range(H)]

    dxdy8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    for x in range(H):
        for y in range(W):
            if S[x][y] == '.':
                res = 0
                for dx, dy in dxdy8:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '#':
                        res += 1
                S[x][y] = str(res)

    for row in S:
        print(''.join(row))

    return


if __name__ == '__main__':
    main()
