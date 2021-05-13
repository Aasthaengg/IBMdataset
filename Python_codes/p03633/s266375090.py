def main():
    from functools import reduce

    N = int(input())

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a // gcd(a, b) * b

    ret = reduce(lcm, (int(input()) for _ in range(N)))
    print(ret)


if __name__ == '__main__':
    main()
