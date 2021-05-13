def solve():
    n, k = map(int, input().split())
    return 1 if n % k else 0


if __name__ == "__main__":
    print(solve())
