from collections import Counter
import sys
sys.setrecursionlimit(10 ** 6)


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
# X = input()
X = list(map(int, list(input())))
one = Counter(X)[1]


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

# x = int(X, 2)
# for i in range(N):
#     ans = dfs(x ^ (1 << ((N - 1) - i)))
#     print(ans)
for i in range(N):
    if one == 1:
        if X[i] == 0:
            m = (Sp + pow(2, N - 1 - i, mp)) % mp
            if m == 0:
                print(1)
            else:
                print(1 + dfs(m))
        else:
            print(0)
        continue

    if X[i] == 0:
        m = (Sp + pow(2, N - 1 - i, mp)) % mp
    else:
        m = (Sm - pow(2, N - 1 - i, mm)) % mm
    
    if m == 0:
        print(1)
    else:
        print(1 + dfs(m))
