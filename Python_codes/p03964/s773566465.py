def solve():
    N = int(input())

    LIS = []
    for _ in range(N):
        LIS.append(tuple(map(int, input().split())))
    # print(LIS)

    A, B = 1, 1
    for (x, y) in LIS:
        # print("current:", A, B)
        # print("ratio  :", x, y, "\n")
        if x == y:
            m = max(x, max(A, B))
            A, B = m, m
        elif A <= x and B <= y:
            A, B = x, y
        else:
            # div = max(ceil(A / x), ceil(B / y)) 誤差でWAになる
            div = max((A + x - 1) // x, (B + y - 1) // y)
            A = x * div
            B = y * div

    return A + B


if __name__ == '__main__':
    res = solve()
    print(res)
