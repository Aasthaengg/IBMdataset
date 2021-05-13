import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import ceil
def main():
    n, a, b, c, d, e = map(int, readlines())
    mint = min(a, b, c, d, e)
    if n <= mint:
        r = 5
    else:
        r = 4 + ceil(n / mint)
    print(r)

if __name__ == '__main__':
    main()
