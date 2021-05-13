# -*- coding: utf-8 -*-

def main():
    x, y = map(int, input().split())

    # どちらも正またはどちらも負の場合
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        # 目標の方が大きければ、ひたすら加算
        if x < y:
            ans = y - x
        # 目標の方が小さければ、符号判定して加算し、符号を戻す。
        else:
            ans = x - y + 2

    # x が 0 のパターン
    elif x == 0:
        # 目標が正なら、ひたすら加算。目標が負なら反転が必要
        if y > 0: ans = y
        else: ans = abs(y) + 1

    # y が 0 のパターン
    elif y == 0:
        # 開始が負なら、ひたすら加算。開始が正なら反転が必要
        if x < 0: ans = abs(x)
        else: ans = x + 1

    # 正負が不一致の場合
    else:
        # 反転1回と差の絶対値回数の加算が必要
        ans = abs(abs(x) - abs(y)) + 1

    print(ans)

if __name__ == "__main__":
    main()
