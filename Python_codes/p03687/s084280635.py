import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    chars = list(set(s))
    ans = INF

    for char in chars:
        t = s[:]
        cnt = 0
        while True:
            if len(set(t)) == 1:
                ans = min(ans, cnt)
                break
            l = len(t)
            r = ""
            for i in range(l - 1):
                if t[i] == char or t[i + 1] == char:
                    r += char
                else:
                    r += t[i]
            cnt += 1
            t = r

    print(ans)


if __name__ == '__main__':
    main()
