def solve():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    print(x * min(n, k) + y * max(n-k,0))


if __name__ == "__main__":
    solve()
