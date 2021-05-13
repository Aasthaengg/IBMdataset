def solve():
    a, b = map(int, input().split())
    return a + b if b % a == 0 else b - a


if __name__ == "__main__":
    print(solve())
