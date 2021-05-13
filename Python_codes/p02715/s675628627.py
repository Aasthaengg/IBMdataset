N, K = map(int, input().split())
mod = 10 ** 9 + 7
G = [1] * (K + 1)  #そのindexを最大公約数にもつ数列の数
ans = 0
for k in range(K, 0, -1):
    x = K // k
    t = int(pow(x, N, mod))
    for j in range(x - 1):
        t -= G[(j + 2) * k]
    G[k] = t
    ans += t * k
    ans %= mod

print(ans)



