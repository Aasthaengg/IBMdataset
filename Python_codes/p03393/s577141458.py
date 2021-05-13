import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from string import ascii_lowercase

    s = input()
    if s == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    elif len(s) < 26:
        x = set(ascii_lowercase) - set(s)
        x = list(x)
        x.sort()
        print(s + x[0])
    else:
        for i in range(25, -1, -1):
            j = 0
            while chr(ord(s[i]) + j + 1) <= "z":
                j += 1
                if chr(ord(s[i]) + j) not in set(s[:i]):
                    return print(s[:i] + chr(ord(s[i]) + j))


if __name__ == '__main__':
    main()
