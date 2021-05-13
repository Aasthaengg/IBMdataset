import math
A, B = map(int, input().split())


def prime_factorize(n):
    a = [1]
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
    a.sort()
    return a

#「公約数は最大公約数の約数」
# ans = 最大公約数の素因数の個数

# A,Bの最大公約数
temp = math.gcd(A, B)
# 最大公約数を素因数分解する
temp = prime_factorize(temp)
# setにして重複除く
temp = set(temp)
# 長さを取得
ans = len(list(temp))

print(ans)
