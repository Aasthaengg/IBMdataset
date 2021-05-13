import sys
import collections
import bisect


def main():
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    k = 0
    ans = 0
    for i in range(n):
        k += a[i]
        if k > x:
            print(ans)
            return
        ans += 1
    print(ans if sum(a) == x else ans - 1)


if __name__ == '__main__':
    main()
