# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    # 標準入力を取得
    N = int(input())
    a = list(map(int, input().split()))

    return N, a


def main(N: int, a: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): マスの数
        a (list): 各マスに書かれた整数
    """
    # 求解処理
    ans = 0
    for i in range(0, N, 2):
        ans += (a[i] % 2 == 1)

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, a = get_input()

    # メイン処理
    main(N, a)
