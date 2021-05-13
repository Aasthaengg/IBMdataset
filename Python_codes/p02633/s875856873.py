mod = 1000000007
eps = 10**-9


def main():
    import sys
    from math import gcd
    input = sys.stdin.readline

    x = int(input())
    print(360 // gcd(360, x))
    

if __name__ == '__main__':
    main()
