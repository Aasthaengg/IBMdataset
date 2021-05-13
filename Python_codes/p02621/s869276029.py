N = 5 * 10**6


def f(x):
    return x


M = 10**5
arr = list(range(M))
for i in range(N):
    t = (i + i * i - i) % M  # 四則演算
    b = arr[t]  # 配列ランダムアクセス
    b = f(b)  # 関数呼び出し

# 答え
a = int(input())
print(a + a**2 + a**3)
