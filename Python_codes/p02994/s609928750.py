import numpy as np

n,l = map(int,input().split())
taste = []
taste_diff = []

for i in range(1,n+1):
    taste.append(l+i-1)

#print(taste)
s = sum(taste)

for i in range(len(taste)):
    taste_diff.append(s-taste[i])

#print(taste_diff)

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

print(getNearestValue(taste_diff, s))

