import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import ceil
def main():
    n, k = map(int, input().split())
    if k == 1:
        print(0)
        sys.exit()
    r1 = n % k
    r2 = abs(r1 - k)
    r = min(r1, r2)
    print(r)


if __name__ == '__main__':
    main()
