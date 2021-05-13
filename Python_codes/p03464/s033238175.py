from math import ceil, floor

K = int(input())
A = list(map(int, input().split()))


"""
- X人いてAi人グループをつくるとき，floor(X/Ai)個のグループになる
- floor(X/Ai) * Ai = X - X mod Ai 人が残る
- fp(X) = X - X mod pとする
"""

L, R = 2, 2

# L, Rから1つ前のL, R (最小，最大)を復元する

for k in range(K - 1, -1, -1):
    # print(k, A[k])
    L = ceil(L / A[k]) * A[k]
    R = floor(R / A[k]) * A[k] + A[k] - 1
    if L > R:
        print(-1)
        exit()

print(L, R)