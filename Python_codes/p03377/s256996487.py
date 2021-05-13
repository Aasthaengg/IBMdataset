def solve():
    A, B, X = map(int, input().split())
    if A <= X <= A + B:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    solve()
