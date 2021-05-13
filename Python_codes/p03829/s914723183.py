def solve():
    N, A, B = map(int, input().split())
    Xi = tuple(map(int, input().split()))

    # print(N, "\n徒歩疲労度", A, "\nテレポ疲労度", B)
    # print(Xi)

    total = 0
    for i in range(1, N):
        total += min((Xi[i] - Xi[i - 1]) * A, B)

    return total


if __name__ == '__main__':
    res = solve()
    print(res)
