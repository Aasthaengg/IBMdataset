import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    A = [0] * N
    for i in range(N):
        A[i] = [int(s) - 1 for s in reversed(readline().split())]

    S = set()

    def check(i):
        if not A[i]:
            return
        j = A[i][-1]
        if i == A[j][-1]:
            if i > j:
                i, j = j, i
            S.add((i, j))

    for i in range(N):
        check(i)

    day = 0
    matches = 0
    while S:
        day += 1
        S, S_prev = set(), S
        for i, j in S_prev:
            A[i].pop()
            A[j].pop()
            matches += 1
        for i, j in S_prev:
            check(i)
            check(j)

    if matches == N * (N - 1) // 2:
        ans = day
    else:
        ans = -1

    print(ans)
    return


if __name__ == '__main__':
    main()
