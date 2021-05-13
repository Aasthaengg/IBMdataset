def solve():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    y = list(map(int, input().split()))
    y.append(Y)

    if max(x) < min(y):
        print('No War')
    else:
        print('War')


if __name__ == '__main__':
    solve()
