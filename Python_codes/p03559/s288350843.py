import sys
import bisect

readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    C = list(map(int, readline().split()))

    A.sort()
    C.sort()

    ans = 0
    for b in B:
        tmpa = bisect.bisect_left(A, b)
        tmpc = N - bisect.bisect_right(C, b)
        ans += tmpa*tmpc
    print(ans)


if __name__ == "__main__":
    main()
