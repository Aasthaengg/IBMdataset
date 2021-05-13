N, M = map(int, input().split())
key = [[] for _ in range(M)]
for i in range(M):
    a, _ = map(int, input().split())
    # 空けることができる宝箱をbitで表す
    c = 0
    for v in list(map(int, input().split())):
        c += pow(2, v-1)
    key[i] = [a, c]

status_count = pow(2, N)
INF = 10 ** 30
# keyの各要素の先頭が値段になってる
dp = [INF] * (status_count)
dp[0] = 0
for a, c in key:
    # 今対象の鍵を購入したときの最小値を求める
    for i in range(status_count):
        dp[i | c] = min(dp[i | c], dp[i] + a)

print(dp[-1] if dp[-1] < INF else -1)
