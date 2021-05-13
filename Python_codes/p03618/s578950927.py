import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    s = input()
    l = len(s)
    counter = Counter()
    ans = 1

    for i in range(l):
        char = s[i]
        ans += i - counter[char]
        counter[char] += 1

    print(ans)


if __name__ == '__main__':
    main()
