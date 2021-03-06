import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import accumulate
from bisect import bisect
def main():
    n, m, k = map(int, input().split())
    a = tuple(accumulate(map(int, input().split())))
    b = tuple(accumulate(map(int, input().split())))
    r = bisect(b, k)

    for i1, ae in enumerate(a):
        if k < ae:
            break
        r = max(r, bisect(b, k - ae) + i1 + 1)
    print(r)

if __name__ == '__main__':
    main()