import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, read().split())
    s = ["#" * w] + ["w" + read() + "w" for _ in range(h)] + ["w" * w]
    left = [[0] * (w + 2) for _ in range(h + 2)]
    right = [[0] * (w + 2) for _ in range(h + 2)]
    up = [[0] * (w + 2) for _ in range(h + 2)]
    down = [[0] * (w + 2) for _ in range(h + 2)]
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if s[y][x] == ".":
                left[y][x] = left[y][x - 1] + 1
                up[y][x] = up[y - 1][x] + 1
            if s[-y - 1][-x - 1] == ".":
                right[-y - 1][-x - 1] = right[-y - 1][-x] + 1
                down[-y - 1][-x - 1] = down[-y][-x - 1] + 1
    c = 0
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if s[y][x] == ".":
                c = max(left[y][x] + right[y][x] + up[y][x] + down[y][x], c)
    print(c - 3)


if __name__ == '__main__':
    main()
