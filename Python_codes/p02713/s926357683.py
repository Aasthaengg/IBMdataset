import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import gcd
def main():
    k = int(input())
    r = 0
    for i1 in range(1, k + 1):
        for i2 in range(1, k + 1):
            for i3 in range(1, k + 1):
                t1 = gcd(i1, i2)
                r += gcd(t1, i3)
    print(r)

if __name__ == '__main__':
    main()