# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    A, B, C = list(map(int, input().split()))
    K = int(input())

    return A, B, C, K

def main(A: int, B: int, C: int, K: int) -> None:
    """
    メイン処理.

    Args:\n
        A (int): 整数（1 <= A <= 7）
        B (int): 整数（1 <= B <= 7）
        C (int): 整数（1 <= C <= 7）
        K (int): 操作回数（1 <= K <= 7）
    """
    # 求解処理
    cnt = 0
    while A >= B:
        cnt += 1
        B *= 2
    while B >= C:
        cnt += 1
        C *= 2

    # 結果出力
    if cnt <= K:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    # 標準入力を取得
    A, B, C, K = get_input()

    # メイン処理
    main(A, B, C, K)
