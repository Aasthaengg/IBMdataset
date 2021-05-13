def solve():
    D, N = [int(i) for i in input().split()]
    print(f"{N if N != 100 else N + 1}{'00' * D}")

if __name__ == "__main__":
    solve()
