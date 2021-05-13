from numba import jit
import sys
input = sys.stdin.readline


@jit
def solve(n, k, X):
    for _ in range(k):
        Y = [0]*(n+1)
        for i, x in enumerate(X):
            Y[max(0, i-x)] += 1
            Y[min(n, i+x+1)] -= 1
        for j in range(1, n):
            Y[j] += Y[j-1]
        if X == Y[:-1]:
            break
        X = Y[:-1]
    return X


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = solve(N, K, A)
    print(*ans)


if __name__ == '__main__':
    main()
