import sys

input = sys.stdin.readline


def main():
    A = list(map(int, input().split()))

    cost_1 = abs(A[1] - A[0]) + abs(A[2] - A[1])
    cost_2 = abs(A[2] - A[0]) + abs(A[1] - A[2])
    cost_3 = abs(A[0] - A[1]) + abs(A[2] - A[0])
    cost_4 = abs(A[2] - A[1]) + abs(A[0] - A[2])
    cost_5 = abs(A[0] - A[2]) + abs(A[1] - A[0])
    cost_6 = abs(A[1] - A[2]) + abs(A[0] - A[1])

    ans = min(cost_1, cost_2, cost_3, cost_4, cost_5, cost_6)
    print(ans)


if __name__ == "__main__":
    main()
