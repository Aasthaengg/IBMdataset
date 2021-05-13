def solve():
    for row in range(H):
        for col in range(W):
            if (row < B and col < A) or (B <= row and A <= col):
                print(0, end='')
            else:
                print(1, end='')
        print()

if __name__ == "__main__":
    H, W, A, B = map(int, input().split())
    solve()