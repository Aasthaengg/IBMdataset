# ARC084C - Snuke Festival
import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

def main():
    n = int(input())
    A, B, C = [sorted(map(int, input().rstrip().split())) for _ in range(3)]
    l, ans = len(C), 0
    for i in B:
        ans += bisect_left(A, i) * (l - bisect_right(C, i))
    print(ans)


if __name__ == "__main__":
    main()