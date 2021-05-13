import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = input()
    l = len(n)

    ans = 0
    x = int(n)
    while x > 0:
        ans += x % 10
        x //= 10

    else:
        for i in range(l):
            score = 0
            for j in range(i):
                score += int(n[j])
            score += int(n[i]) - 1
            score += 9 * (l - (i + 1))
            ans = max(score, ans)

    print(ans)


if __name__ == '__main__':
    main()
