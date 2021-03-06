import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    H, W, M = map(int, input().split())

    row = [0] * H
    col = [0] * W
    bomb = set()

    for i in range(M):
        h, w = map(int, input().split())
        h -= 1
        w -= 1
        row[h] += 1
        col[w] += 1
        bomb.add((h, w))

    # print(row, col, bomb)

    rowmax = max(row)
    colmax = max(col)

    rows = []
    cols = []
    for i in range(H):
        if row[i] == rowmax:
            rows.append(i)
    for i in range(W):
        if col[i] == colmax:
            cols.append(i)

    for r in rows:
        for c in cols:
            if (r, c) in bomb:
                continue
            else:
                print(rowmax + colmax)
                exit()

    print(rowmax + colmax - 1)


if __name__ == "__main__":
    main()
