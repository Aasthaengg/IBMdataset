from math import factorial as fct
def main():
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    b = K
    r = N - K
    for i in range(1, K+1):
        p_blue = (fct((b-i)+(i-1)) // fct(b-i) // fct(i-1)) % MOD
        if r >= i-1:
            p_red = (fct((r-(i-1))+i) // fct(r-(i-1)) // fct(i)) % MOD
        else:
            p_red = 0
        print((p_blue * p_red) % MOD)
main()