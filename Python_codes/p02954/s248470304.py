import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    N = len(S)

    A = list(range(N))
    for _ in range(10):
        for i, a in enumerate(A):
            if S[a] == 'L':
                A[i] -= 1
            else:
                A[i] += 1

    B = A
    for _ in range(99):
        A, B = B, list(range(N))
        for _ in range(10):
            for i, b in enumerate(B):
                B[i] = A[b]

    ans = [0] * N
    for b in B:
        ans[b] += 1

    print(*ans)
    return


if __name__ == '__main__':
    main()
