import itertools
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N, M, D = list(map(int, sys.stdin.readline().split()))


# 数列の 1 つ目の要素が決まれば数も決まりそう
# 差が D となる数が上にだけある・下にだけある・上にも下にもある・どっちにもない
# 1 <= a <= N-D までは上にある
# D < a <= N までは下にある

def solve(n, m, d):
    arr = list(itertools.product(range(n), repeat=m))
    ans = 0
    for a in arr:
        for i in range(m - 1):
            if abs(a[i] - a[i + 1]) == d:
                ans += 1
    return ans


# 隣り合う要素を 2 つ決めたときに差が D となる組み合わせの数
if D == 0:
    c = N
else:
    c = (N - D) * 2

# # 全部の合計
# # pow(N, M - 2): ある 2 つの要素を決めたときにその位置にそれらを使う数列の数
# s = c * pow(N, M - 2) * (M - 1)
# # 個々の美しさがわからなくても合計がわかれば組み合わせ数で割れば平均になる
# ans = s / pow(N, M)

# ans = c * (M - 1) * pow(N, M - 2) / pow(N, M)
ans = c * (M - 1) / N ** 2
print(ans)
