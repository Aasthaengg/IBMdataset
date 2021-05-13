import sys


def query(S):
    print(S)
    sys.stdout.flush()
    return input()


def main():
    N = int(input())
    base = query(0)
    if base == "Vacant":
        return
    lo = 1
    hi = N-1
    while lo < hi:
        mid = (lo+hi) // 2
        ans = query(mid)
        if ans == "Vacant":
            return
        if (mid % 2 == 0 and ans == base) or \
           (mid % 2 == 1 and ans != base):
            lo = mid + 1
        else:
            hi = mid
    query(lo)


if __name__ == "__main__":
    main()
