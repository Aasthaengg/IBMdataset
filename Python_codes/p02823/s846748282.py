def solve():
    N, A, B = [int(i) for i in input().split()]
    if (A - B) % 2 == 0:
        print(abs(A - B) // 2)
    else:
        ans1 = ((N - A) + (N - B) + 1) // 2
        ans2 = ((A - 1) + (B - 1) + 1) // 2
        print(min(ans1, ans2))

if __name__ == "__main__":
    solve()
