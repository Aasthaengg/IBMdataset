def solve():
    A, B, C, D = map(int, input().split())
    return max(A * B, C * D)


if __name__ == '__main__':
    res = solve()
    print(res)
