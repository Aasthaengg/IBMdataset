from bisect import bisect_left
def main():
    h, w, m = map(int, input().split())
    bombs = set()
    cnt_row, cnt_col = [0]*(h+1), [0]*(w+1)
    for _ in range(m):
        y, x = map(int, input().split())
        cnt_row[y] += 1
        cnt_col[x] += 1
        bombs.add((y, x))
    max_cnt_row = max(cnt_row)
    max_cnt_col = max(cnt_col)
    idx_row = []
    idx_col = []
    for i in range(h+1):
        if cnt_row[i] == max_cnt_row:
            idx_row.append(i)
    for j in range(w+1):
        if cnt_col[j] == max_cnt_col:
            idx_col.append(j)
    ans = max_cnt_row + max_cnt_col - 1
    for i in idx_row:
        for j in idx_col:
            if not (i, j) in bombs:
                ans = max_cnt_row + max_cnt_col
                break
    print(ans)

if __name__ == "__main__":
    main()