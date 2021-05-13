import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = []
    for _ in range(N):
        x, y = map(int, input().split())
        A.append((x, y))
    if N == 1:
        print(1)
        return

    A.sort()
    import collections
    D = collections.defaultdict(int)
    import itertools
    for a, b in itertools.combinations(A, 2):
        p = a[0] - b[0]
        q = a[1] - b[1]
        D[(p, q)] += 1
    d = sorted(D.values())
    print(N - d[-1])


if __name__ == '__main__':
    main()
