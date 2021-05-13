from math import gcd
def inv(n, p):
    """
    mod p の逆元
    """
    return pow(n, p-2, p)
def lcm(a, b):
    return a*b//gcd(a,b)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    LCM = 1
    for a in A:
        LCM = lcm(LCM, a)
    ans = 0
    for a in A:
        ans += inv(a, mod)
    ans *= LCM % mod

    print(ans % mod)
main()