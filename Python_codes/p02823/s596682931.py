import sys
n, a, b = map(int, input().split())

# 2で割って余り1ならすれ違わない
if (b - a) % 2 == 0:
    print((b - a) // 2)

else:
    # 左で折り返す場合
    left = ((a - 1) + (b - 1) + 1) // 2

    # 右で折り返す場合
    right = ((n - b) + (n - a) + 1) // 2

    print(min(left, right))