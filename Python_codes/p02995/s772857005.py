import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import gcd
def main():
    a, b, c, d = map(int, input().split())
    if a == b:
        if a % c != 0 and a % d != 0:
            print(1)
            sys.exit()
        else:
            print(0)
            sys.exit()
    atob = b - a + 1
    divc = b // c - (a - 1) // c
    divd = b // d - (a - 1) // d
    cd = c * d // gcd(c, d)
    divcd = b // cd - (a - 1) // cd
    r = atob - divc - divd + divcd
    print(r)


if __name__ == '__main__':
    main()