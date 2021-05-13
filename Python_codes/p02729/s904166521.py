N, M = map(int, input().split())
# N 個の偶数 と　M個の奇数

# 2個選ぶ=偶数になる->2個とも偶数か2個とも奇数
print(N * (N - 1) // 2 + M * (M - 1) // 2)