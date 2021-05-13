N, M = map(int, input().split())
ans = 0

#Sが全部使える場合
if 2*N <= M:
    ans += N
    M -= 2*N
    #余ったCの取り扱い。Mが4個でSccを一個作れる。
    ans += M//4

#Cが足りないのでSを全部使えない場合
else:
    ans += M//2

print(ans)
