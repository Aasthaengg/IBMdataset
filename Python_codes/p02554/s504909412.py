# -*- coding: utf-8 -*-

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
        N (int): 整数(1 <= N <= 10**6)
    """
    # 求解処理
    ans = 10**N - 2 * 9**N + 8**N
    ans %= 10**9 + 7

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N = get_input()

    # メイン処理
    main(N)
