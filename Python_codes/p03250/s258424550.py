def solve():
    x = list(map(int, input().split()))
    x.sort()
    print(x[2] * 10 + x[1] + x[0])


if __name__ == '__main__':
    solve()
