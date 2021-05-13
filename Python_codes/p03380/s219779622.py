import math
import numpy as np

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

n = int(input())
a = [int(i) for i in input().split()]
check = 0
a.sort()
b = a[-1]
c = getNearestValue(a,b/2)
ans = str(b) + ' ' + str(c)
print(ans)