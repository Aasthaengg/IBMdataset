import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    kn = [int(x) for x in input().rstrip().split(" ")]
    k = kn[0]
    a = [int(x) for x in input().rstrip().split(" ")]

    max_dist = max([a[i+1] - a[i] for i in range(len(a)-1)])
    max_dist = max_dist if max_dist > a[0] + k - a[len(a)-1] else a[0] + k - a[len(a)-1]

    print(k - max_dist)


if __name__ == "__main__":
    resolve()
