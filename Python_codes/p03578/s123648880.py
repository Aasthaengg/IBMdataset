import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    dList = list(map(int, readline().rstrip().split()))
    m = int(readline().rstrip())
    tList = list(map(int, readline().rstrip().split()))
    dc = collections.Counter(dList)
    tc = collections.Counter(tList)
    tcKeys = list(tc.keys())
    for tcKey in tcKeys:
        if dc[tcKey] < tc[tcKey]:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()
