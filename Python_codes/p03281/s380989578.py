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
        N (int): 1以上200以下の整数
    """
    # 求解処理
    ans = 0
    for n in range(1, N + 1, 2):
        divisors_count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divisors_count += 1
        if divisors_count == 8:
            ans += 1

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N = get_input()

    # メイン処理
    main(N)
