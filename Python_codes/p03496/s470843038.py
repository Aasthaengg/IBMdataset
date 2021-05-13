import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    Amax, Amin = max(A), min(A)
    imax, imin = A.index(Amax), A.index(Amin)

    ans = []
    rev = False

    if Amax <= 0:
        rev = True
    elif Amax > 0 and Amin < 0:
        if Amax >= abs(Amin):
            for i in range(N):
                if A[i] < 0:
                    A[i] += Amax
                    ans.append((imax, i))
        else:
            rev = True
            for i in range(N):
                if A[i] > 0:
                    A[i] += Amin
                    ans.append((imin, i))

    if not rev:
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                A[i + 1] += A[i]
                ans.append((i, i + 1))
    else:
        for i in range(N - 1, 0, -1):
            if A[i] < A[i - 1]:
                A[i - 1] += A[i]
                ans.append((i, i - 1))

    print(len(ans))
    for x, y in ans:
        print(x + 1, y + 1)

    return


if __name__ == '__main__':
    main()
