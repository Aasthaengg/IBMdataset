def solve():
    N, M = list(map(int, input().split()))

    remain_c = M - N * 2

    if remain_c <= 0:
        return M // 2
    else:
        return N + (remain_c // 4)


if __name__ == '__main__':
    res = solve()
    print(res)
