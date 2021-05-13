import numpy as np

n = int(input())
a = list(map(int, input().split()))

a.sort()


def get_nearest_value(arr, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(arr) - num).argmin()

    return arr[idx]


first = a[-1]
second = get_nearest_value(a, first / 2)

print(first, second)
