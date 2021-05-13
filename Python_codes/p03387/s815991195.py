# vim: fileencoding=utf-8

import math


def main():
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    m = li[0] - li[1]
    n = li[0] - li[2]
    p = n - m
    ans = m + math.ceil(p / 2) + (p % 2)
    print(ans)


if __name__ == "__main__":
    main()
