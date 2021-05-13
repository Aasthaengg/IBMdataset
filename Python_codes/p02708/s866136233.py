import math
N, K = map(int, input().split())
mod = 10**9+7

ans = 0
for k in range(K, N+2):
    #個数が異なると合計も変わるので毎度計算する
    #数列の小さい方からk個選ぶ
    min_part = (k-1)*k//2
    #数列の大きい方からk個選ぶ
    max_part = (N*(N+1)-(N-k)*(N-k+1))//2
    #差分を足す
    ans += max_part-min_part+1
    
    ans %= mod


print(ans)


