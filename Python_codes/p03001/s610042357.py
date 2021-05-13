import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    W, H, x, y = map(int, input().split())

    area = W * H * 0.5
    res = 0
    if W % 2 == 0 and H % 2 == 0 and x == W // 2 and y == H // 2:
        res = 1

    print(area, res)


if __name__ == '__main__':
    solve()
