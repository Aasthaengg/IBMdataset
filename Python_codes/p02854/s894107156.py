import sys
from itertools import accumulate

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    cumsum_A = list(accumulate(A))
    sum_A = sum(A)

    ans = float("inf")
    for i in range(N - 1):
        # cost = abs((sum_A - cumsum_A[i]) - cumsum_A[i])
        cost = abs(sum_A - 2 * cumsum_A[i])
        if cost < ans:
            ans = cost

    print(ans)


if __name__ == "__main__":
    main()
