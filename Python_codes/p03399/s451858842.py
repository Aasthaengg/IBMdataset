def solve():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    print(min(A + C, A + D, B + C, B + D))


if __name__ == "__main__":
    solve()
