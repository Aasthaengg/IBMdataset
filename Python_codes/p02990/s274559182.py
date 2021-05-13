N,K = map(int,input().split())
# iこの入れる場所の選び方(N-K+1)Ci,Kこの間にi-1この仕切を入れると考える
# よって(N-K+1)Ci * (K-1)C(i-1)が求める答えになる
ans = 0
L = 10**9 + 7
# pythonは一行ずつ前からしか読めないからそこんとこ注意
import math
# ライブラリは実行される前に書いておくこと
def comb(n,i):
    ans = 1
    for j in range(i):
        ans *= (n-j)
        ans %= L
    div = math.factorial(i)
    div %= L
    div = pow(div,L-2,L)
    ans *= div
    ans %= L
    return ans

for i in range(1,K+1):
    ans = comb(N-K+1,i) * comb(K-1,i-1)
    ans %= L
    print(ans)





