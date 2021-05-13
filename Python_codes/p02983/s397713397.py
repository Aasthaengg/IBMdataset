import sys
from itertools import combinations

MOD = 2019


def solve(l, r):
    if l // 673 != r // 673 or l % 673 == 0:
        if l // 3 != r // 3 or l % 3 == 0:
            return 0
    ans = 10000
    for i, j in combinations(range(l, r + 1), 2):
        ans = min(ans, i * j % MOD)
    return ans


def main():
    input = sys.stdin.buffer.readline
    l, r = map(int, input().split())
    print(solve(l, r))


if __name__ == "__main__":
    main()
