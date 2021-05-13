def d_grid_components(H=100, W=100):
    A, B = [int(i) for i in input().split()]
    # グリッドの縦と横は入力に関わらず定数 (条件の最大値) とする
    # 100x100 グリッドの上半分を黒で，下半分を白で塗りつぶす
    grid = [['#'] * W for _ in range(50)] + [['.'] * W for _ in range(50)]

    def fill(start, end, num, symbol):
        """start 行から end-1 行まで，num 個の symbol を 1 マスおきに置いていく"""
        for row in range(start, end, 2):
            for col in range(1, W, 2):
                if num == 0:
                    return
                grid[row][col] = symbol
                num -= 1
        return None

    fill(1, 50, A - 1, '.')  # 黒ゾーンに 1 つおきに 1x1 白マスを A-1 個置く
    fill(51, 100, B - 1, '#')  # 白ゾーンに 1 つおきに 1x1 黒マスを B-1 個置く
    return '100 100\n' + '\n'.join([''.join(row) for row in grid])

print(d_grid_components())