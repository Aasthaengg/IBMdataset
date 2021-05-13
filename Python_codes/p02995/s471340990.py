def main():
    from math import gcd
    a, b, c, d = (int(i) for i in input().split())
    L = c*d//gcd(c, d)
    ans = b - (b//c + b//d - b//L)
    ans -= (a-1) - ((a-1)//c + (a-1)//d - (a-1)//L)
    print(ans)


if __name__ == '__main__':
    main()
