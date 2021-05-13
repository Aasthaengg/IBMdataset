from pprint import pprint
import sys

K = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

ls = len(S)


mod = 10**9 + 7
MAX = ls + K + 100
factorial = [1] * (MAX+1)
t = 1
for i in range(1, MAX+1):
    t = (t * i) % mod
    factorial[i] = t
def combination(n, x, mod=10**9+7):
    # nCx
    # 組み合わせ
    # ex) combination(5, 2) = 10
    # factorial = [1] * (n+1)
    # t = 1
    # for i in range(1, n+1):
    #     t = (t * i) % mod
    #     factorial[i] = t
    tmp = factorial[n]
    tmp = (tmp * pow(factorial[x], mod-2, mod)) % mod
    tmp = (tmp * pow(factorial[n-x], mod-2, mod)) % mod
    return tmp



# Sの部分文字列を埋め込む場所のパターン
# S + K choose S

# Snを配置する場所ごとに全パターンを計算
ans = 0
for i in range(ls-1, ls + K):	
    tmp = pow(25, i-ls+1, mod) 
    tmp *= pow(26, ls + K - i - 1, mod) 
    comb = combination(i, ls-1)
    tmp *= comb
    tmp %= mod
    ans += tmp
    ans %= mod

print(ans)