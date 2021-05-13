import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    K = int(readline())

    subs = set()

    S_sorted = sorted(set(S))
    for c_min in S_sorted:
        indices = [i for i, c in enumerate(S) if c == c_min]
        for i in indices:
            for j in range(i + 1, min(len(S) + 1, i + K + 1)):
                subs.add(S[i:j])

        if len(subs) >= K:
            break

    subs = sorted(subs)
    print(subs[K - 1])

    return


if __name__ == '__main__':
    main()
