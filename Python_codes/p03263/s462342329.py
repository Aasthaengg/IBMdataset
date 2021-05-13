import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    h, w = map(int, read().split())
    a = [[int(i) for i in read().split()] for _ in range(h)]
    b = []
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if a[i - 1][j - 1] % 2 == 0:
                continue
            if j < w:
                # a[i - 1][j - 1] -= 1
                a[i - 1][j] += 1
                b.append((i, j, i, j + 1))
            elif i < h:
                # a[i - 1][j - 1] -= 1
                a[i][j - 1] += 1
                b.append((i, j, i + 1, j))
    print(len(b))
    for bi in b:
        print(*bi)


if __name__ == '__main__':
    main()