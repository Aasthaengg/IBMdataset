# -*- coding: utf-8 -*-
# モジュールのインポート
import math


def get_input() -> int:
    """
    標準入力を取得する.

    Returns:\n
        int: 標準入力
    """
    N = int(input())

    return N


def main(N: int) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 正整数(2 <= N <= 10**6)
    """
    # 求解処理
    ans = 0
    for a in range(1, N):
        ans += math.floor((N - 1) / a)

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N = get_input()

    # メイン処理
    main(N)
