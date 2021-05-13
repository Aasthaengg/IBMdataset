from typing import List


def solve(A: List[int], N: int) -> int:
    current_money = 1000
    for i in range(N - 1):
        stocks = 0

        if A[i] < A[i + 1]:
            stocks = current_money // A[i]
        current_money += (A[i + 1] - A[i]) * stocks
    return current_money


def main():
    N = int(input())
    A = [int(x) for x in input().split(" ")]

    print(solve(A, N))


if __name__ == "__main__":
    main()
