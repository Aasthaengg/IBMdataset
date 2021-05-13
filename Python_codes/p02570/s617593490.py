def solve():
    D, T, S = map(int, input().split())
    if T * S >= D:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solve()