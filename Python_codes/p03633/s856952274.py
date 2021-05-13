import sys
read = sys.stdin.read
from math import gcd
def main():
    n = int(input())
    t = [int(input()) for _ in range(n)]
    if n == 1:
        print(t[0])
        sys.exit()
    r = (t[0] * t[1]) // gcd(t[0], t[1])
    if n == 2:
        print(r)
        sys.exit()
    for i1 in range(2, n):
        r = (r * t[i1]) // gcd(r, t[i1])
    print(r)

if __name__ == '__main__':
    main()

