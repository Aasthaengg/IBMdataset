import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 1
    cnt = [0, 0, 0]
    for a in A:
        if a not in cnt:
            print(0)
            return
        i = cnt.index(a)
        c = cnt.count(a)
        cnt[i] += 1
        ans *= c
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
