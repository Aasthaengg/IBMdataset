import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import accumulate
def main():
    n, k, *p = map(int, read().split())
    p2 = [0] + [(1 + pe) / 2 for pe in p]
    r = 0
    p2a = tuple(accumulate(p2))
    for i1 in range(k, n+1):
        r = max(r, p2a[i1] - p2a[i1-k])
    print(r)

if __name__ == '__main__':
    main()
