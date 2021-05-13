def solve():
    A, B = map(int, input().split())

    # print(A, B)

    return (A + B) % 24


if __name__ == '__main__':
    res = solve()
    print(res)
