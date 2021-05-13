from collections import Counter
import sys
sys.setrecursionlimit(10 ** 6)


# パート2 の解法
def dfs(n):
    if memo[n] >= 0:
        rst = memo[n]
    else:
        tmp = n
        one = 0
        while tmp > 0:
            one += tmp & 1
            tmp >>= 1
        m = n % one
        rst = 1 if m == 0 else 1 + dfs(m)
        memo[n] = rst
    return rst


N = int(input())
X = list(map(int, list(input())))
one = Counter(X)[1]

# パート1の解法.
# Xがオール0のとき, 1が一つしか含まれないとき、を場合分けする
if one > 1:
    Sm = 0
    mm = one - 1
    tm = 1
    for i in range(N - 1, -1, -1):
        tm %= mm
        if X[i] == 1:
            Sm += tm
            Sm %= mm
        tm *= 2

Sp = 0
mp = one + 1
tp = 1
for i in range(N - 1, -1, -1):
    tp %= mp
    if X[i] == 1:
        Sp += tp
        Sp %= mp
    tp *= 2


memo = [-1] * (2 * (10 ** 5) + 10)
memo[0] = 0

for i in range(N):
    # 解法パート1
    if X[i] == 0:
        m = (Sp + pow(2, N - 1 - i, mp)) % mp
    elif one > 1:
        m = (Sm - pow(2, N - 1 - i, mm)) % mm
    else:  # X[i] == 1 かつ 全体で1が一つしかない 場合 は必ず0になる
        print(0)
        continue
    cnt = 1

    # 解法パート2
    cnt += dfs(m)
    print(cnt)