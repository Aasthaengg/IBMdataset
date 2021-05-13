def solve():
    A = list(map(int, input().split()))
    A.sort()
    cost = 0
    cost += A[1] - A[0]
    cost += A[2] - A[1]
    print(cost)


if __name__ == "__main__":
    solve()
