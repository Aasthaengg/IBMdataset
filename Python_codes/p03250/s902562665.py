import sys
from itertools import permutations
def input(): return sys.stdin.readline().strip()


def main():
    a, b, c = map(int, input().split())
    ans = 0
    for p, q, r in list(permutations([a, b, c])):
        ans = max(ans, 10 * p + q + r, p + 10 * q + r)
    print(ans)


if __name__ == "__main__":
    main()
