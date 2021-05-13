# -*- coding: utf-8 -*-

def get_input() -> int:
    """
    標準入力を取得する.

    Returns:\n
        int: 標準入力
    """
    N = int(input())

    return N


def divisor_count(n: int) -> int:
    """
    引数の約数の個数を取得する.

    Args:\n
        n (int): 引数

    Returns:\n
        int: 約数の個数
    """
    ans = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans += 1
            if i != n // i:
                ans += 1
        i += 1
    return ans


def main(N: int) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 整数（1 <= N <= 200）
    """
    # 求解処理
    ans = 0
    for n in range(1, N + 1, 2):
        if divisor_count(n) == 8:
            ans += 1

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N = get_input()

    # メイン処理
    main(N)
