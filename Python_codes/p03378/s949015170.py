def solve():
    N, M, X = map(int, input().split())
    A = map(int, input().split())
    squares = [0 for _ in range(0, N+1)]
    for a in A:
        squares[a] = 1
    print(min(squares[:X].count(1), squares[X+1:].count(1)))


if __name__ == "__main__":
    solve()