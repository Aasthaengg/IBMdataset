n, k = map(int, input().split())
a = list(map(int, input().split()))

# imos法で区間和を計算する、をk回まで繰り返す
cnt = 0
while cnt < k:
    imos = [0] * (n + 1)
    for i in range(n):
        imos[max(i - a[i], 0)] += 1
        imos[min(i + a[i] + 1, n)] -= 1

    for i in range(n):
        imos[i + 1] += imos[i]

    a = imos[0:n]
    cnt += 1

    if min(a) == n:
        # a = [n, n, n, ..., n] になったら打ち切り
        break
print(*a)
