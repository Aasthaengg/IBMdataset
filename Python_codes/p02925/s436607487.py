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
        A[i] = [int(s) - 1 for s in readline().split()]

    M = N * (N - 1) // 2

    total_mathces = 0
    changed = set(range(N))
    for day in range(M):
        matches = 0
        changed_prev, changed = changed, set()
        for i in changed_prev:
            if i in changed or not A[i]:
                continue
            j = A[i][-1]
            if j not in changed and i == A[j][-1]:
                changed.add(i)
                changed.add(j)
                A[i].pop()
                A[j].pop()
                matches += 1

        if matches == 0:
            ans = -1
            break

        total_mathces += matches
        if total_mathces == M:
            ans = day + 1
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
