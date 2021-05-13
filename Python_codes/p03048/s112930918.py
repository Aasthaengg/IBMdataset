# -*- coding: utf-8 -*-
# 標準入力の取得
R, G, B, N = list(map(int, input().split()))


def main() -> None:
    """Entry point
    """
    # 求解処理
    """
    r, gをそれぞれ固定して探索を行う.
    """
    r_max = N // R
    g_max = N // G
    result = 0
    for r in range(r_max+1):
        n_r = r * R
        for g in range(g_max+1):
            n_rg = n_r + g * G
            # この時点でNよりも大きい場合、何もしない
            if N < n_rg:
                continue
            # Nまでの不足分がBで割り切れる場合、条件を満たしたことになる
            if (N - n_rg) % B == 0:
                result += 1

    # 結果出力
    print(result)


if __name__ == "__main__":
    main()
