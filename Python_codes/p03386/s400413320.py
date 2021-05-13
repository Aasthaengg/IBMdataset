def solve():
    A, B, K = [int(i) for i in input().split()]
    for i in range(A, B + 1):
        if i < A + K or i > B - K:
            print(i)

if __name__ == "__main__":
    solve()