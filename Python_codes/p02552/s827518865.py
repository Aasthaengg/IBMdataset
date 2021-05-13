# -*- coding: utf-8 -*-

def get_input() -> int:
    """
    標準入力を取得する.

    Returns:\n
        int: 標準入力
    """
    x = int(input())

    return x


def main(x: int) -> None:
    """
    メイン処理.

    Args:\n
        x (int): 整数(0 <= x <= 1)
    """
    # 求解処理
    ans = 1 - x

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    x = get_input()

    # メイン処理
    main(x)
