# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N = int(input())
    D_1, D_2 = [], []
    for i in range(N):
        D_i1, D_i2 = list(map(int, input().split()))
        D_1.append(D_i1)
        D_2.append(D_i2)

    return N, D_1, D_2


def main(N: int, D_1: list, D_2: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): サイコロを振った回数(3 <= N <= 100)
        D_1 (list): i回目の出目(1 <= D_i1 <= 6)
        D_2 (list): i回目の出目(1 <= D_i2 <= 6)
    """
    # 求解処理
    ans = "No"
    doublet_cnt = 0
    for i in range(N):
        if D_1[i] == D_2[i]:
            doublet_cnt += 1
        else:
            doublet_cnt = 0

        if doublet_cnt >= 3:
            ans = "Yes"
            break

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, D_1, D_2 = get_input()

    # メイン処理
    main(N, D_1, D_2)
