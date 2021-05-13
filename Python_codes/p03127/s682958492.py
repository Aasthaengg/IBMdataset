import sys
read = sys.stdin.read
from math import gcd
def main():
    n, *a = map(int, read().split())
    r = gcd(a[0], a[1])
    if n == 2:
        print(r)
        sys.exit()
    for i1 in range(2, n):
        r = gcd(r, a[i1])
    print(r)

if __name__ == '__main__':
    main()
