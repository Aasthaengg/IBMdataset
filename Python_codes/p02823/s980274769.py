def solve():
    N, A, B = [int(i) for i in input().split()]
    if (B - A) % 2 == 0:
        print((B - A) // 2)
    else:
        print(min(N - B, A - 1) + 1 + (B - A - 1) // 2)

if __name__ == "__main__":
    solve()