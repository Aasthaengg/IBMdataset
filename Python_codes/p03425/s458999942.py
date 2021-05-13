import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = [readline().strip() for _ in range(N)]

    initials = set('MARCH')
    counter = Counter()
    for s in S:
        if s[0] in initials:
            counter[s[0]] += 1

    vec = list(counter.values())
    ans = 0
    for i in range(len(vec) - 2):
        for j in range(i + 1, len(vec) - 1):
            for k in range(j + 1, len(vec)):
                ans += vec[i] * vec[j] * vec[k]

    print(ans)
    return


if __name__ == '__main__':
    main()
