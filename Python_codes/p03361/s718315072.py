import numpy as np


def main():
    h, w = map(int, input().split())
    sss = [list(input()) for _ in range(h)]
    check = [[0 for _ in range(w)] for _ in range(h)]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    sharp_count = 0
    for i in range(h):
        for j in range(w):
            if sss[i][j] == '#':
                sharp_count += 1
                for k, l in move:
                    if i+k < h and i+k >= 0 and j+l < w and j+l >= 0:
                        if sss[i+k][j+l] == "#":
                            check[i][j] = 1
                            check[i+k][j+l] = 1
    if sharp_count == np.sum(check):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
