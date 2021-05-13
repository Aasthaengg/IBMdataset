# https://atcoder.jp/contests/abc129/tasks/abc129_d
from copy import deepcopy
def main():
    h, w = map(int, input().split())
    matrix = []
    for _ in range(h):
        row = list(input())
        matrix.append(row)

    left = [[0] * w for _ in range(h)] # 左から右
    right = [[0] * w for _ in range(h)] # 右から左
    up = [[0] * w for _ in range(h)] # 上から下
    down = [[0] * w for _ in range(h)] # 下から上

    for i in range(h):
        c = 0
        for j in range(w):
            if matrix[i][j] == '.':
                c += 1
            else:
                c = 0
            left[i][j] = c
    for i in range(h):
        c = 0
        for j in range(w)[::-1]:
            if matrix[i][j] == '.':
                c += 1
            else:
                c = 0
            right[i][j] = c
    for j in range(w):
        c = 0
        for i in range(h):
            if matrix[i][j] == '.':
                c += 1
            else:
                c = 0
            up[i][j] = c
    for j in range(w):
        c = 0
        for i in range(h)[::-1]:
            if matrix[i][j] == '.':
                c += 1
            else:
                c = 0
            down[i][j] = c
    ans = 1
    for i in range(h):
        for j in range(w):
            t = left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3
            ans = max(ans, t)
    print(ans)

if __name__ == "__main__":
    main()