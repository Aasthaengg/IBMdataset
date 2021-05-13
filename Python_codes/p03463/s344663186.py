def solve(N, A, B):
    d1 = A - 1
    d2 = B - A - 1
    d3 = N - B

    if d2 % 2 == 1:
        return "Alice"
    else:
        return "Borys"
        # if d1 == 0 and d2 == 0:
        # if d1 % 2 == 0 and d3 % 2 == 0:
        #     return "Borys"
        # else:
        #     return "Draw"


if __name__ == "__main__":
    N, A, B = tuple(map(int, input().split(" ")))
    print(solve(N, A, B))
