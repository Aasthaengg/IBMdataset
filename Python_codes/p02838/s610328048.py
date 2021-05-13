def main():
    from itertools import zip_longest
    n, *a = map(lambda x: bin(int(x))[2:][::-1], open(0).read().split())
    n = int('0b' + n[::-1], 2)

    mod = 10 ** 9 + 7
    ans = 0
    
    for i, j in enumerate(zip_longest(*a)):
        o = j.count('1')
        z = n - o
        ans += z * o * pow(2, i, mod)
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
