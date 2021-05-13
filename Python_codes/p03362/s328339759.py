# coding: utf-8

# https://atcoder.jp/contests/abc096/tasks/abc096_d
# 16:51-


def prime_set(limit=10**5):
    """
    2020/04/10
    https://atcoder.jp/contests/abc084/tasks/abc084_d
    """

    ret = [2]
    for x in range(3, limit+1, 2):
        is_prime = True
        sqrtx = int(pow(x, 0.5))

        for p in ret:
            if p > sqrtx:
                break

            if x % p == 0:
                is_prime = False
                break

        if is_prime:
            ret.append(x)

    return ret


def main():
    N = int(input())

    primes = prime_set(55555)
    
    ans = [None] * N
    i = 0
    for p in primes:
        if p % 5 == 2:
            ans[i] = p
            if i == N-1:
                break
            i += 1

    for a in ans:
        print(a, end=" ")


main()
# print(main())
