# -*- coding: utf-8 -*-
# 標準入力の取得
N = int(input())
A = int(input())


def main() -> None:
    """Entry point
    """
    # 求解処理
    """
    500円で割ったあまりと1円の枚数を比較
    """
    result = str()
    if (N % 500) <= A:
        result = "Yes"
    else:
        result = "No"

    # 結果出力
    print(result)


if __name__ == "__main__":
    main()
