import sys
import numpy as np

n = int(input())

a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

# 総和が足りなければ合格できない
if a.sum() < b.sum():
    print(-1)
    sys.exit()

diff = a - b

# 初めから条件を満たしている場合
if np.where(diff < 0)[0].shape[0] == 0:
    print(0)
    sys.exit()

# プラス要素とマイナス要素に分離する。0はいじらなくてよい
minus = diff[np.where(diff < 0)]
plus = diff[np.where(diff > 0)]

# マイナスの要素をプラスの成分が大きい方から消化していく
ans = minus.shape[0]
sum_minus = np.abs(minus).sum()
plus.sort()
plus = plus[::-1]
plus = plus.cumsum()

# 何個目のプラスまでで消化しきれるか
ans += np.where(plus >= sum_minus)[0].min() + 1

print(ans)