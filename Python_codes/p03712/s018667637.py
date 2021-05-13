def solve():
    H, W = [int(i) for i in input().split()]
    print("#" * (W + 2))
    for _ in range(H):
        print(f"#{input()}#")
    print("#" * (W + 2))

if __name__ == "__main__":
    solve()