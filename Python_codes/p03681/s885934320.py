from math import factorial

N, M = map(int, input().split())
mod = 10**9+7

if abs(N-M) > 1:
    print(0)
    quit()

else:
    if N == M:
        #犬猿or猿犬をひとかたまりとして考える。
        NM_half = N
        #犬猿どっちが右かを区別する
        ans = 2
        # ans %= mod 
        #個別の犬、猿がどこに立つかを考慮する
        ans *= factorial(N)
        ans %= mod
        ans *= factorial(M)
        ans %= mod

        print(ans)
    else:
        ans = factorial(N)
        ans %= mod
        ans *= factorial(M)
        ans %= mod

        print(ans)
