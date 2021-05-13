# https://atcoder.jp/contests/abc052/tasks/arc067_b
# 歩いたほうが良いのかテレポートしたほうが良いのか貪欲に選択していくだけでは？

import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))



N, A, B = read_ints()
X = read_ints()

# 面倒なのでnumpy芸してええか？
X_diff = [x-y for x,y in zip(X[1:],X[:-1])]
ans = 0
for d in X_diff:
    ans += min(B, d * A)
print(ans)
