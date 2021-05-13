# -*- coding: utf-8 -*-
# モジュールのインポート
import math


def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    # 標準入力を取得
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    return N, K, A


def main(N: int, K: int) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 数列の長さ(2 <= K <= N <= 10**5)
        K (int): 選択する要素数(2 <= K <= N <= 10**5)
    """
    # 求解処理
    ans = math.ceil((N - 1) / (K - 1))

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, K, A = get_input()

    # メイン処理
    main(N, K)
