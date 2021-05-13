def solve(n, m):

    return (n-2 if n-2 >= 0 else 1) * (m-2 if m-2 >= 0 else 1)

if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    print(solve(n, m))
