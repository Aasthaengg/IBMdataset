# 問題文の意味がわからんコンテスト
# 0の場合も自分自身を照らす、っての気づくところからやっと読解
# Kを5000兆回やったあとはすべての要素がNになっとる この収束はわりと早いらしい
n, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(min(k, 100)):
    b = [0] * (n + 1)
    for i in range(n):
        b[max(0, i - a[i])] += 1
        b[min(n, i + a[i] + 1)] -= 1
    for i in range(n):
        b[i + 1] += b[i]
    a = b[:n]
print(" ".join(list(map(str, a))))