# 2043
# 2114 解法 X,Yについて素因数分解をする．お互いに共通の素因数の数＋１が答えになるのでは？
# 約数はどっちにしても素因数もしくはその倍数になる．互いに素な共役数で素因数と合成数の両方を持つことはできないので
# 共通な素因数をたし上がればいい
# 実装
def prime_fac(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

X, Y = map(int,input().split())
X_prime = set(prime_fac(X))
Y_prime = set(prime_fac(Y))
Common = X_prime & Y_prime
print(1+len(Common))

