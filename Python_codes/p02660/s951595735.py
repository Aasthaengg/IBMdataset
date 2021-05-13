# まあできるだけ小さい単位で割ったほうが嬉しいので、素因数分解して因数で割ったほうがうれしい
# ただし以前つかったやつは使えないので、x^1, x^2, x^3... に限定されてしまう
# -> 冪数を増やしていく感じでいけそう

n = int(input())


def div_primes(x):
    ret = {}
    for i in range(2, int(x**0.5) + 1):
        tmp = 0
        while x % i == 0:
            tmp += 1
            x /= i
        if tmp > 0:
            ret[i] = tmp

    if x > 1:
        ret[x] = 1
    return ret


primes = div_primes(n)
ans = 0
for k, v in primes.items():
    j = 1
    while v - j >= 0:
        v -= j
        j += 1
        ans += 1
print(ans)