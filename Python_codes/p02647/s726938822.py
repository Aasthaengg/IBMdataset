from numba import jit
import sys
input = sys.stdin.readline


@jit
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(K):
        B = [0]*(N+1)
        for i, a in enumerate(A):
            B[max(0, i-a)] += 1
            B[min(N, i+a+1)] -= 1
        for j in range(1, N):
            B[j] += B[j-1]
        if A == B[:-1]:
            A = B[:-1]
            break
        A = B[:-1]

    ans = ' '.join(list(map(str, A)))
    print(ans)


if __name__ == '__main__':
    main()
