import sys
from collections import Counter
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    R, G, B, N = [int(n) for n in input().strip().split()]
    ans = 0
    for r in range((N//R)+1):
        for g in range((N-(R*r)//G)+1):
            if (N - (R * r) - (G * g)) % B == 0 and (N - (R * r) - (G * g)) // B >= 0:
                ans += 1
    return ans


if __name__ == '__main__':
    print(main())
