import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
def main():
    h, w, m = map(int, input().split())
    b_row = [0] * h
    b_col = [0] * w
    b_coor = set()
    m = map(int, read().split())
    for a, b in zip(m, m):
        a -= 1
        b -= 1
        b_row[a] += 1
        b_col[b] += 1
        b_coor.add((a, b))

    row_max = max(b_row)
    col_max = max(b_col)
    rows = [i for i, v in enumerate(b_row) if v == row_max]
    cols = [i for i, v in enumerate(b_col) if v == col_max]

    for r in rows:
        for c in cols:
            if (r, c) not in b_coor:
                print(row_max + col_max)
                sys.exit()
    print(row_max + col_max - 1)

if __name__ == '__main__':
    main()
