import sys
input = sys.stdin.readline

def main():
    h, w, m = map(int, input().split())
    bomb_row = [0] * h
    bomb_col = [0] * w
    # 座標だけはsetで格納
    bomb_pos = set()
    # 爆弾情報を行と列ごとで格納
    for _ in range(m):
        r, c = [int(i) - 1 for i in input().split()]
        bomb_row[r] += 1
        bomb_col[c] += 1
        bomb_pos.add((r,c))

    bomb_row_max = max(bomb_row)
    bomb_col_max = max(bomb_col)

    row_index = [i for i, v in enumerate(bomb_row) if v == bomb_row_max]
    col_index = [i for i, v in enumerate(bomb_col) if v == bomb_col_max]
    ans = bomb_col_max + bomb_row_max
    for row in row_index:
        for col in col_index:
            if (row, col) not in bomb_pos:
                print(ans)
                return
    print(ans-1)
main()