import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = list(input())
    k = int(readline())
    l = len(s)
    rem = k

    for i in range(l):
        char = s[i]
        diff = (ord("z") - ord(s[i]) + 1) % 26
        if rem >= diff:
            rem -= diff
            s[i] = "a"

    rem = rem % 26
    s[l - 1] = chr(ord(s[l - 1]) + rem)
    print("".join(s))


if __name__ == '__main__':
    main()
