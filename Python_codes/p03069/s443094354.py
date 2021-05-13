import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().strip()

    c = collections.Counter(S)
    c2 = collections.Counter()
    ans = min(c['.'], c['#'])

    for i in range(N):
        c2[S[i]] += 1
        ans = min(ans, c2['#'] + c['.'] - c2['.'])

    print(ans)


if __name__ == '__main__':
    main()
