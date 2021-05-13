def solve():
    X = int(input())
    memo = {}
    for A in range(500):
        for B in range(500):
            memo[A**5-B**5] = (A,B)
            memo[A**5+B**5] = (A,-B)
    A,B = memo[X]
    print(A, B)

if __name__ == "__main__":
    solve()