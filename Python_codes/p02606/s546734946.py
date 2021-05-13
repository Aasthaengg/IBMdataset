# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    L, R, d = list(map(int, input().split()))

    return L, R, d


def main(L: int, R: int, d: int) -> None:
    """
    メイン処理.

    Args:\n
        L (int): 整数（1 <= L <= R <= 100）
        R (int): 整数（1 <= L <= R <= 100）
        d (int): 整数（1 <= d <= 100）
    """
    # 求解処理
    ans = R // d - (L - 1) // d

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    L, R, d = get_input()

    # メイン処理
    main(L, R, d)
