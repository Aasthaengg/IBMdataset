import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)

MOD = (10**9) + 7


def main():
    ans = 1
    N = int(input().strip())
    for n in range(1, N + 1):
        ans *= n
        ans = ans % MOD
    return ans


if __name__ == "__main__":
    print(main())