import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
from bisect import bisect_left
def main():
    n, *l = map(int, read().split())
    l.sort()
    r = n * (n - 1) * (n - 2) // 6
    for i1 in range(n - 2):
        for i2 in range(i1 + 1, n - 1):
            r -= (n - bisect_left(l, l[i1] + l[i2]))
    print(r)

if __name__ == '__main__':
    main()