n, m, d = map(int, input().split())

# 隣接する要素の期待スコア x (n-1) が答え (それぞれ独立)
# i, j が 1..n を取る時，個数は n * n
# そのうち絶対の差がdになるものは n * 2個？#
#
# n = 2, d = 1
# 1 1 -> 0
# 1 2 -> 1
# 2 1 -> 1
# 2 2 -> 0
# score は 2，期待値は0.5，長さは3なので，0.5 x (3-1) = 1.0
#
# この組が何個あるか，をdとnに依存して正しく求める
#
# n = 10, d = 3
# 1 -> 4
# 2 -> 5
# 3 -> 6
# 4 -> 1, 7
# 5 -> 2, 8
# 6 -> 3, 9
# 7 -> 4, 10
# 8 -> 5
# 9 -> 6
# 10 -> 7

if d == 0:
    fact = 1 / n
else:
    fact = 2 * (n - d) / (n * n)
score = fact * (m - 1)
print("{:.10f}".format(score))