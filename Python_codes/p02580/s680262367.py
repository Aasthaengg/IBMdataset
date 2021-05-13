def main():
    H, W, M = map(int, input().split())
    bomb_row = [0 for _ in range(H)]  # 爆弾が何行目に何個あるか
    bomb_column = [0 for _ in range(W)]  # 爆弾が何列目に何個あるか
    bomb_map = set()  # 爆弾がどこにあるか

    for _ in range(M):
        r, c = map(int, input().split())
        bomb_row[r - 1] += 1
        bomb_column[c - 1] += 1
        bomb_map.add((r - 1, c - 1))

    max_row = max(bomb_row)  # 行ごとに見て最も多い爆弾の個数
    max_column = max(bomb_column)  # 列ごとに見て最も多い爆弾の個数
    ans = max_row + max_column

    bomb_max_row = []  # 爆弾がmax_row個ある行
    bomb_max_column = []  # 爆弾がmax_column個ある列

    for i in range(H):
        if bomb_row[i] == max_row:
            bomb_max_row.append(i)
    for i in range(W):
        if bomb_column[i] == max_column:
            bomb_max_column.append(i)

    for r in bomb_max_row:
        for c in bomb_max_column:
            if (r, c) not in bomb_map:  # 最多行と最多列の交点に爆弾が無ければ終了
                print(ans)
                return

    print(ans - 1)  # 最多行と最多列の交点に爆弾があればans - 1


if __name__ == "__main__":
    main()
