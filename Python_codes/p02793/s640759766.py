def main():
    from fractions import gcd

    MOD = 10 ** 9 + 7

    N = int(input())
    A = list(map(int, input().split()))

    tmp = 1
    for a in A:
        tmp *= a // gcd(tmp, a)

    ans = 0
    for a in A:
        ans += (tmp // a)
    ans %= MOD

    print (ans)

if __name__ == '__main__':
    main()