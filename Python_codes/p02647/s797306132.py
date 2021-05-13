from numba import jit
import sys
input = sys.stdin.readline


@jit
def solve(n, k, A):
    for _ in range(k):
        B = [0]*(n+1)
        for i, a in enumerate(A):
            B[max(0, i-a)] += 1
            B[min(n, i+a+1)] -= 1
        for j in range(1, n):
            B[j] += B[j-1]
        if A == B[:-1]:
            break
        A = B[:-1]
    return A


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = solve(n, k, A)
    print(*ans)


if __name__ == '__main__':
    main()
