# https://atcoder.jp/contests/abc175/submissions/15965930

def main():
    import sys
    input = sys.stdin.readline

    H, W, K = map(int, input().split())

    G = [[0] * W for _ in range(H)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        G[r - 1][c - 1] = v

    dp0 = [0] * (W + 1)
    dp1 = [0] * (W + 1)
    dp2 = [0] * (W + 1)
    dp3 = [0] * (W + 1)
    # dpx:=行内取得x個以下の最大値
    # <cは更新済の同じ行の値
    # c<=は前の行の値

    for r in range(H):
        for c in range(W):
            v = G[r][c]

            dp0[c] = max(dp0[c], dp3[c])  # 垂直移動
            vertical_take = dp0[c] + v  # 垂直移動+(r,c)取得

            dp3[c] = max(dp3[c - 1], dp2[c - 1] + v, vertical_take)
            dp2[c] = max(dp2[c - 1], dp1[c - 1] + v, vertical_take)
            dp1[c] = max(dp1[c - 1], dp0[c - 1] + v, vertical_take)
            # 水平移動（左）から来て取らない
            # 水平移動（左）から来て取る
            # 垂直移動で来て取らない:=dp0
            # 垂直移動で来て取る:=dpx(x>0)

            # print(f'{dp0=}')
            # print(f'{dp1=}')
            # print(f'{dp2=}')
            # print(f'{dp3=}')
            # print('*******************')

    print(dp3[-2])


if __name__ == '__main__':
    main()
