# vim: fileencoding=utf-8

import math


def main():
    n, c, k = map(int, input().split())
    t = []
    for x in range(n):
        t.append(int(input()))
    t.sort()
    ans = 0
    bucket = []
    for i in t:
        while len(bucket) >= c:
            ans += 1
            bucket = bucket[c:]
        while len(bucket) > 0 and bucket[0] + k < i:
            ans += 1
            bucket = bucket[c:]
        bucket.append(i)
    ans += math.ceil(len(bucket) / c)
    print(ans)


if __name__ == "__main__":
    main()
