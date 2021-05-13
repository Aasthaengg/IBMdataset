import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()
    c = collections.Counter(S)

    for i in range(26):
        if c[chr(ord('a') + i)] == 0:
            print(S + chr(ord('a') + i))
            return

    for j in range(len(S) - 1, -1, -1):
        x = ord(S[j]) - ord('a')
        c[S[j]] -= 1
        for i in range(x + 1, 26):
            if c[chr(ord('a') + i)] == 0:
                print(S[:j] + chr(ord('a') + i))
                return

    print(-1)


if __name__ == '__main__':
    main()
