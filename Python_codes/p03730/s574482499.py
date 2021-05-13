import sys
read = sys.stdin.read
from math import gcd
def main():
    a, b, c = map(int, input().split())
    gac = gcd(a, -b)
    if c % gac == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
