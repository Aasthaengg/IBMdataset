def main():
    from math import factorial
    n = int(input())
    mod = 10 ** 9 + 7
    nf = factorial(n)
    l = f(nf)
    ans = 1
    for x in l:
        ans *= (x + 1)
    ans %= mod
    print(ans)


def f(n):
    l = []
    for i in range(2, n + 1):
        if n == 1:
            break
        count = 0
        while n % i == 0:
            n = n // i
            count += 1
        if count > 0:
            l.append(count)
    return l


if __name__ == '__main__':
    main()
