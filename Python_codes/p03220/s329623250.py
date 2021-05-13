import numpy as np

def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return idx


n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))

temp = []

for i in range(n):
    temp_var = t - h[i] * 0.006
    temp.append(temp_var)

print(getNearestValue(temp,a) + 1)