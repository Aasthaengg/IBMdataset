import sys
from itertools import combinations


def main():
    input = sys.stdin.buffer.readline
    _n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i, j in combinations(d, 2):
        ans += i * j
    print(ans)


if __name__ == "__main__":
    main()

