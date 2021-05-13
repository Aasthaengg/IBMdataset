def d_grid_components(A, B):  # 白マス,黒マスの連結成分の個数
    H, W = 100, 100  # グリッドの縦と横。入力に関わらず定数(条件の最大値)とする
    # 100x100グリッドの上半分を黒で、下半分を白で塗りつぶす
    grid = [['#'] * W for _ in range(50)] + [['.'] * W for _ in range(50)]

    def fill(start, end, num, symbol):
        # start列からend-1列まで、num個のsymbolを1マスおきに置いていく
        for h in range(start, end, 2):
            for w in range(1, W, 2):
                if num > 0:
                    grid[h][w] = symbol
                    num -= 1
                else:
                    return
        return None

    fill(1, 50, A - 1, '.')  # 黒ゾーンに1つおきに1x1白マスをA-1個置く
    fill(51, 100, B - 1, '#')  # 白ゾーンに1つおきに1x1黒マスをB-1個置く

    ans = '100 100\n' + '\n'.join([''.join(row) for row in grid])
    return ans

A, B = [int(i) for i in input().split()]
print(d_grid_components(A, B))