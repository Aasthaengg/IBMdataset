def resolve():
    n = int(input())
    M = 10 ** 9 + 7
    pl = [0] * (n + 1)

    for i in range(2, n+1):
        x = i
        p = 2
        while x > 1:
            while x % p == 0:
                pl[p] += 1
                x //= p
            p += 1
    ans = 1
    for s in pl:
        ans *= (s+1)

    print(ans % M)

if __name__ == '__main__':
    resolve()