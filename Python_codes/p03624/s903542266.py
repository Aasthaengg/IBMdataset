import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    found = [0] * 26
    for c in S:
        found[ord(c) - ord('a')] = True

    ans = 'None'
    for i, f in enumerate(found):
        if not f:
            ans = chr(i + ord('a'))
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
