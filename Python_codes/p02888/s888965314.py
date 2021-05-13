import sys
from bisect import bisect_left

input = sys.stdin.readline


def solve(N, L):
    L.sort()
    ans = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            c = bisect_left(L, L[a] + L[b]) - 1
            ans += c - b
    return ans


def main():
    N = int(input())
    L = list(map(int, input().split()))

    ans = solve(N, L)
    print(ans)


if __name__ == "__main__":
    main()
