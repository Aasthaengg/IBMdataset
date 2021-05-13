import sys
from fractions import Fraction
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    deno = 0
    for i in a:
        deno += Fraction(1, i)
    print(float(1/deno))

if __name__ == '__main__':
    main()