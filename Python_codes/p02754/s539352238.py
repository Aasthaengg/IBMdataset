def solve():
    N,A,B = [int(i) for i in input().split()]
    blue_red = A + B
    ans = N // blue_red * A + min(A, N % blue_red)
    print(ans)

if __name__ == "__main__":
    solve()