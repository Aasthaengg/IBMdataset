import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    s1 = input()
    s2 = input()

    if n == 1:
        print(3)
        return

    ans = 3 * 2

    for i in range(2, n):
        if s1[i-1] == s2[i-1]:
            ans *= 2
        else:
            if s1[i-1] == s1[i-2]:
                if s1[i] == s2[i]:
                    ans *= 1
                else:
                    ans *= 3
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
