import math


def solve(N, D):
    return math.ceil(N / (2 * D + 1))


if __name__ == "__main__":
    # N = int(input())
    # Vs = list(map(int, input().split(" ")))
    N, D = tuple(map(int, input().split()))
    print(solve(N, D))
