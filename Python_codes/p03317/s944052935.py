import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import ceil
def main():
    n, k, *a = map(int, read().split())
    if n <= k:
        print(1)
        sys.exit()
    else:
        r = ceil((n - 1) / (k - 1))
        print(r)
if __name__ == '__main__':
    main()