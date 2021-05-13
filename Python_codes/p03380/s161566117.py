import sys
import bisect

readline = sys.stdin.readline

def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    if len(a) == 2:
        a.sort(reverse=True)
        print(*a)
        return
    amax = a.pop()
    mid = amax//2
    mididx = bisect.bisect_left(a, mid)
    am1 = a[mididx]; am2 = a[mididx-1]
    if abs(am1-mid) <= abs(am2-mid):
        am = am1
    else:
        am = am2
    print(amax, am)


if __name__ == "__main__":
    main()
