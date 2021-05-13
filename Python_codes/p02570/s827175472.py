import math


def solve(D, T, S):
    minutes = math.ceil(D / S)
    ans = 'Yes' if T >= minutes else 'No'
    print(ans)


if __name__ == "__main__":
    D, T, S = map(int, input().split())
    solve(D, T, S)
