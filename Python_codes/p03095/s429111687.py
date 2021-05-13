from collections import Counter
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    n = int(input().strip())
    S = input().strip()
    cnts = Counter(S)

    x = 1
    for v in cnts.values():
        x *= (v + 1)
    ans = x - 1

    MOD = 10**9 + 7

    print(ans % MOD)
    return


if __name__ == "__main__":
    main()