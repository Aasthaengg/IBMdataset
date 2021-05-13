n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0  # f(x)の最大値
x = 0 ## x(十進数)

## A_i <= 10**12なので A_i <= 2**40→２進数で41桁以下
for i in range(40, -1, -1): ## i <- 40, 39, 38, ... , 0 
    c = 0
    for ai in a:
        if (ai >> i) & 1: ## ai二進数のi+1桁目が1かどうか
            c += 1  ## すべてのaiについてi+1桁目の1の個数
            
    ### n-c「すべてのaiについてのi+1桁目の０の個数」が１の個数を上回るかつ
    ### xのi桁目に1を立てたとき十進数でxがk以下
    if (n - c) > c and x + (1 << i) <= k:
        x += 1 << i## xのi桁目は1を立てる。
        ans += (n - c) * (1 << i)## 答えに(n-c)*2^(i)をたす
    else:
        ## xのi桁目は0を立てる
        ans += c * (1 << i)
print(ans)